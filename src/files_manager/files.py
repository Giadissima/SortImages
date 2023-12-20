from hashlib import md5
from os.path import join, exists
from os import remove, rename
from typing import List, Union
from src.date_manager import DateManager
from src.config.config import Config

from src.sort.regex import RegexMedia
from src.files_manager.folders import Folder
class File:
  def __init__(self):
    self.BUF_SIZE = 65536
    self.HASH_LIST = set()
    
  def move_file(self, file_path: str, file_name: str, new_path: str):
    # print(current_path, file, new_path)
    Folder.create_nested_dir(new_path)
    # cambia il nome del file in modo univoco
    file_dest_path = join(new_path, file_name)
    i = 0
    file_list = file_name.rsplit('.', 1)
    
    while exists(file_dest_path):
      file_name = f"{file_list[0]}.{i}.{file_list[1]}"
      file_dest_path = join(new_path, file_name) 
      i+=1
    try:
      rename(file_path, file_dest_path)
      return True
    except PermissionError:
      return False
      
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
  def extract_date(cls, file_path: str, file: str, folder_date: List[str]|None):
    regex = RegexMedia()
    if(folder_date != None and len(folder_date) == 3): 
      # print(folder_date)
      # print(file_path, "founded folder date")
      return folder_date
    date = cls.get_date_from_metadata(file_path)
    # se la data non era contenuta nei metadati allora guardo se la trovo nel nome del media
    if(date != None): 
      return date 
    date = regex.extract_date_from_media(file, folder_date)
    return date
  
  def handle_duplicates(self, file_path, file_name)->Union[bool, str|None]:
    """Checks if the passed file is a duplicate and, 
    if so, examines the action it should take based on 
    the preferences previously entered by the user.
    Args:
      file_path (str): the entire path of the file to check
      file:name (str): just the name of the file to check
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
  
  def handle_move_file(self, media_class, file_path:str, file_name:str, folder_date: str):
    """Checks if the passed date is valid, and if so, creates the new path for the image and moves it."""
    date = media_class.extract_date(file_path, file_name, folder_date)
    
    # case no date found: file not moved
    if(date == None):
      return 'error', f'{file_name} - No date found in the file: file not moved.'
    
    # case date_found
    date_path = DateManager.get_date_path(date, Config.output_folder)
    response = self.move_file(file_path, file_name, date_path)
    if response:
      return 'debug', f'{file_name} - moved successfully.'
    else: 
      return 'error', f'{file_name} - The file could not be moved'