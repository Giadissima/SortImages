from hashlib import md5
from os.path import join, exists
from os import remove, rename
from typing import List, Optional, Union
from src.error.error import FileNotMovedError
from src.path_manager import PathManager
from src.config.config import Config
from src.thread.semaphore import SemaphoreManager

from src.sort.regex.regex_file import RegexMedia
from src.files_manager.folders import Folder
class File:
  def __init__(self):
    self.BUF_SIZE = 65536
    self.HASH_LIST = set()
    self.semaphore = SemaphoreManager()
    self.path_manager = PathManager()
    
  def move_file(self, file_path: str, file_name: str, new_path: str):
    """Move a file in a new directory, and in case of name duplicate error, rename the file.
    Args:
      file_path (string): old file's path,
      file_name(string): name of the file
      new_path (string): new file's path
    """
    if self.semaphore.acquired: return
    self.semaphore.acquire()
    Folder.create_nested_dir(new_path)
    file_dest_path = self.check_file_name(file_name, new_path)
    try:
      rename(file_path, file_dest_path)
    except PermissionError:
      raise FileNotMovedError("Permission Error")
    finally:
      self.semaphore.release()
      
  def isDuplicate(self, file):
    """Find if file is a duplicate by the array contains al the hash previously seen

    Args:
      file (string): file to search duplicates
      path (string): path contains other files
    """ 
    file_hashed = self.hash_file(file)
    if file_hashed in self.HASH_LIST:
      return True
    self.HASH_LIST.add(file_hashed)
    return False
      
  def hash_file(self, file):
    hash = md5()
    with open(file, 'rb') as f:
      while True:
        data = f.read(self.BUF_SIZE)
        if not data:
          break
        hash.update(data)
    return hash.hexdigest()
  
  @classmethod
  def extract_date(cls, file_path: str, file: str, folder_date: List[str]|None)-> Optional[List[str]]:
    """Extract date from metadata and file_name, giving priority in order to:
      - folder_date of lenght 3,
      - metadata (date of creation)
      - file name
      - folder_date of other lengths

    Args:
      cls (ImageHelper|VideoHelper): class to which a file belongs which can be an image or a video
      file_path (str): where file's stored
      file (str): name of the file
      folder_date (List[str] | None): the date from the folder

    Returns:
      [year(str), month(str), day(str)]: date extracted from file and folder
    """
    regex = RegexMedia()
    if(folder_date != None and len(folder_date) == 3 and folder_date[0]!=None): 
      return folder_date
    date = cls.get_date_from_metadata(file_path)
    # se la data non era contenuta nei metadati allora guardo se la trovo nel nome del media
    if(date != None and date[0]!=None): 
      return date 
    date = regex.extract_date_from_media(file, folder_date)
    return date
  
  def handle_duplicates(self, file_path, file_name)->Union[bool, str|None]:
    """Checks if the passed file is a duplicate and, 
    if so, examines the action it should take based on 
    the preferences previously entered by the user.
    Args:
      file_path (str): the entire path of the file to check
      file_name (str): just the name of the file to check
    Returns:
      Union[bool, str|None]: 
        bool: True if file is a duplicate, False otherwise
        str: message to be printed if file is a duplicate
    """
    if self.isDuplicate(file_path): 
      if(Config.get_checkbox_choises('DeleteDuplicates')):
        remove(file_path)
        return True, f'{file_name} - Duplicated detected: successfully deleted.'
      else:
        return True, f'{file_name} - Duplicated detected: file not moved.'
    return False, None
  
  def handle_move_file(self, media_class, file_path:str, file_name:str, folder_date: str)-> Union[str, str]:
    """Checks if the date argument is valid, and if so, creates the new path for the image and moves it.

    Args:
      media_class (ImageHelper|VideoHelper): class to which a file belongs which can be an image or a video
      file_path (str): the entire path of the file
      file_name (str): the name of the file
      folder_date (List[str] | None): date extracted from folder

    Returns:
      Union[function_name(str), message(str)]: log message with a default value stored in function_name with a message
    """
    date = media_class.extract_date(file_path, file_name, folder_date)
    
    dest_folder = self.path_manager.get_output_path(file_path, file_name)
    # case no date found: file not moved
    if date == None or date[0]==None:
      if dest_folder==Config.output_folder:
        return 'warn', f'{file_name} - No date found in the file: file not moved.'
      
    # case date_found
    dest_folder = self.path_manager.get_date_path(date, dest_folder)
    self.move_file(file_path, file_name, dest_folder)
    return 'debug', f'{file_name} - moved successfully.'
    
  def check_file_name(self, file_name, new_path) -> str:
    """Check if file name already exists in destination path, if so, 
    find another name and return it
    
    Args:
      file_name(str): the name of the file
      new_path(str): the path to whitch move the file
    
    Return:
      str: the new path with name checked
    """
    file_dest_path = join(new_path, file_name)
    file_list = file_name.rsplit('.', 1)
    
    i = 0
    while exists(file_dest_path):
      file_name = f"{file_list[0]}.{i}.{file_list[1]}"
      file_dest_path = join(new_path, file_name) 
      i+=1
    return file_dest_path