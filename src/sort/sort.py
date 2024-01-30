from os.path import join
from typing import List, Union
from src.logs.logs_helper import LogsHelper
from src.config.config import Config
from src.files_manager import ImageHelper, VideoHelper, Folder, File
from src.sort.regex import RegexMedia
from os import walk

class Sort():
  """The main class responsible for organizing media."""
  def __init__(self) -> None:
    self.regex = RegexMedia()
    self.file = File()
    self.folder = Folder()
    self.logs = None

  def start_sort(self)->Union[bool, str]:
    """Set up everything necessary to start image sorting,
    beginning with checking if the input and output folders
    have been entered correctly, and ending with logging
    whether the sort occurred successfully or if there were errors.
    
    Returns:
      Union[bool, str]: 
        bool: True if the process has completed without errors, False otherwise, 
        str: error's message, if the pricess has completed without errors, str will be None
      """
    result, msg = Folder.check_input_output_folders(Config.input_folder, Config.output_folder)
    if result == False: return result, msg
    try:
      if self.logs is None:
        self.logs = LogsHelper(Config.logs_obj)
      Config.logs_obj.delete_logs()
      self.logs.tkinter_logger.info('checking existing files in destination folder. It may takes a few minutes')
      self.finding_duplicates_output_folder()
      self.logs.tkinter_logger.info('initial check completed. Starting to sort...')
      self.loop_into_folders()
      self.handle_folders_deletion()
      self.logs.tkinter_logger.info('sorting completed.')
      self.file.HASH_LIST.clear()
    except Exception as e:
      print(e)
      self.handle_exception()
      return False, 'Error sorting images. If the error persists, report it on the GitHub project discussion'
    return True, None

  @staticmethod
  def identify_media(file_path: str) -> Union[ImageHelper, VideoHelper, None]:
    """Identify the type of file passed and return its corresponding class.
      Args:
        file_path (str): The full directory of the file to be identified.
      Returns:
        ImageHelper|VideoHelper|None: None if file doesn't match any class"""
    if ImageHelper.isImage(file_path):
        return ImageHelper()
    elif VideoHelper.isVideo(file_path):
        return VideoHelper()
    return None

  def handle_exception(self)->None:
    """Handles exceptions during file processing."""
    self.logs.log_traceback()
    self.logs.log_tkinter('error','An error occurred: file not sorted. See more information on error_logs.log')
     
  def handle_folders_deletion(self)->None:
    """Manages folder deletion."""
    if Config.get_checkbox_choises('DeleteEmptyFolders'):
      msg = self.folder.delete_empty_folders(Config.input_folder)
      if msg == None:
        self.logs.log_tkinter('info','Empty folders deleted')
      else:
        self.logs.log_tkinter('error',msg)
      
  def loop_into_folders(self)->None:
    """checks if there are media files in each subfolder and, if so, reorganizes them."""
    for root, _, files in walk(Config.input_folder):
      root = root.replace('\\', '/')
      if Config.output_folder == root or Folder.is_nested_dir(Config.output_folder, root): 
        continue
      self.folder_date = self.regex.extract_date_from_folder(root)
      self.loop_into_files(root, files)
      
  def loop_into_files(self, folder_path:str, file_list:List[str]):
    """Reorganizes each individual media by reading metadata and using regex in the file name.
    
    Args:
      folder_path (str): Folder to which the file is stored. 
      file_list List[str]: List of files contained within the folder.

    Returns:
      Optional[List[str]]: file's date if exists, otherwise None
      """
    for file_name in file_list:
      file_path = join(folder_path, file_name).replace('\\', '/')
      try:
        media_class:VideoHelper|ImageHelper = Sort.identify_media(file_path)
        if media_class == None: continue
        
        result, msg = self.file.handle_duplicates(file_path, file_name)
        if result:
          self.logs.log_tkinter('info', msg)
          continue
          
        type_of_log, msg = self.file.handle_move_file(media_class, file_path, file_name, self.folder_date)
        if type_of_log == 'error': self.logs.log_tkinter('error', msg)
        else: self.logs.log_tkinter('debug',msg)
      except IndexError:
        self.logs.log_tkinter('error',f"{file_name} - file without any extension, it cannot be sorted")
      
  def finding_duplicates_output_folder(self)->None:
    """checks if there are media files in each subfolder and, if so, reorganizes them."""
    for root, _, files in walk(Config.output_folder):
      root = root.replace('\\', '/')
      for file_name in files:
        file_path = join(root, file_name).replace('\\', '/')
        result, msg = self.file.handle_duplicates(file_path, file_name)
        if result:
          self.logs.log_tkinter('info', msg)
          continue