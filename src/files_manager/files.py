from hashlib import md5
from os.path import join, exists
from os import remove, rename
from typing import List, Optional, Tuple, Union # Added Union for Optional
from src.sort.media_result_calculator import MediaResultCalculator
from src.error.error import FileNotMovedError
from src.sort.path_manager import PathManager
from src.config.config import Config
from src.thread.semaphore import SemaphoreManager

from src.sort.regex.regex_media import RegexMedia
from src.files_manager.folders import Folder
class File:
  def __init__(self):
    self.BUF_SIZE = 65536
    self.HASH_LIST = set()
    self.semaphore = SemaphoreManager()
    self.path_manager = PathManager()
    self.img_res_calc = MediaResultCalculator()
    
  def move_file(self, file_path: str, file_name: str, new_path: str) -> bool: # Return bool
    """Move a file in a new directory, and in case of name duplicate error, rename the file.
    Args:
      file_path (string): old file's path,
      file_name(string): name of the file
      new_path (string): new file's path
    Returns:
      bool: True if the file was moved, False if it was skipped.
    """
    if self.semaphore.acquired: return False # Indicates not moved
    self.semaphore.acquire()
    Folder.create_nested_dir(new_path)
    file_dest_path = self.check_file_name(file_name, new_path) # Can be None now

    if file_dest_path is None: # File should be skipped
        self.semaphore.release()
        return False # File was skipped

    try:
      rename(file_path, file_dest_path)
      self.img_res_calc.increment_total_media_moved()
      return True
    except PermissionError:
      raise FileNotMovedError("Permission Error")
    finally:
      self.semaphore.release()
      
  def isDuplicate(self, file:str)->bool:
    """Find if file is a duplicate by the array contains al the hash previously seen

    Args:
      file (string): file to search duplicates
      path (string): path contains other files
    Returns:
      bool if file is a duplicate, false otherwise
    """ 
    file_hashed = self.hash_file(file)
    if file_hashed in self.HASH_LIST:
      self.img_res_calc.increment_total_media_duplicates_found()
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
  def extract_date(cls, file_path: str, file: str, folder_date: List[str]|None)-> Optional[Tuple[str, str, str]]:
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
    
    # Priority 1: folder_date if available and complete
    if folder_date is not None and len(folder_date) == 3 and folder_date[0] is not None: 
      return folder_date

    metadata_priority = Config.UI_OPTION_VARS['images_metadata_priority'].get()

    date_from_metadata = None
    date_from_filename = None

    if metadata_priority == "metadata":
        date_from_metadata = cls.get_date_from_metadata(file_path)
        if date_from_metadata is not None and date_from_metadata[0] is not None:
            return date_from_metadata
        date_from_filename = regex.extract_date_from_media(file, folder_date) # Pass folder_date as fallback for filename regex
        if date_from_filename is not None and date_from_filename[0] is not None:
            return date_from_filename
    else: # priority is "file_name"
        date_from_filename = regex.extract_date_from_media(file, folder_date) # Pass folder_date as fallback for filename regex
        if date_from_filename is not None and date_from_filename[0] is not None:
            return date_from_filename
        date_from_metadata = cls.get_date_from_metadata(file_path)
        if date_from_metadata is not None and date_from_metadata[0] is not None:
            return date_from_metadata

    # If nothing found, return None
    return None
  
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
        self.img_res_calc.increment_total_media_deleted()
        return True, 'Duplicated detected: successfully deleted.'
      else:
        return True, 'Duplicated detected: file not moved.'
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
        self.img_res_calc.increment_total_unrecognized_media()
        if Config.get_checkbox_choises("UnknownFolder"):
          dest_folder = join(dest_folder, 'Unknown')
          if self.move_file(file_path, file_name, dest_folder): # Check if moved
            return 'warn', 'No date found: file moved in unknown folder'
          else:
            return 'warn', f"File '{file_name}' skipped due to conflict resolution setting."
        return 'warn', 'No date found: file not moved.'
      
    # case date_found
    was_moved = self.move_file(file_path, file_name, dest_folder)
    
    if was_moved:
        return 'debug', f'moved successfully.'
    else:
        # If not moved, it means it was skipped due to conflict resolution
        return 'info', f"File '{file_name}' skipped due to conflict resolution setting."
    
  def check_file_name(self, file_name, new_path) -> Optional[str]: # Return Optional[str]
    """Check if file name already exists in destination path, if so, 
    find another name and return it based on conflict resolution setting.
    
    Args:
      file_name(str): the name of the file
      new_path(str): the path to which move the file
    
    Return:
      Optional[str]: the new path with name checked, or None if file should be skipped
    """
    file_dest_path = join(new_path, file_name)
    
    if not exists(file_dest_path):
        return file_dest_path

    # File exists, apply conflict resolution
    conflict_resolution = Config.UI_OPTION_VARS['conflict_resolution_method'].get()

    if conflict_resolution == "overwrite":
        return file_dest_path # Overwrite
    elif conflict_resolution == "skip":
        return None # Skip
    elif conflict_resolution == "rename":
        file_list = file_name.rsplit('.', 1)
        i = 0
        while exists(file_dest_path):
            # Ensure we handle files without extensions correctly
            if len(file_list) > 1:
                file_name = f"{file_list[0]}.{i}.{file_list[1]}"
            else: # No extension, just append counter
                file_name = f"{file_list[0]}.{i}"
            file_dest_path = join(new_path, file_name) 
            i+=1
        return file_dest_path
    return file_dest_path # Default to rename if something unexpected happens