from logging import Logger
from os.path import join
from threading import Event
import time
from typing import Union
from src.files_manager.folders import Folder
from src.config.config import Config
from src.files_manager.folders import Folder
from src.sort.regex import RegexMedia
from src.files_manager.images import ImageHelper
from src.files_manager.video import VideoHelper
from src.files_manager.files import File
from os import remove, walk, listdir
from src.logs import get_error_logger, get_tkinter_logger

# TODO rivedere i file di imports
# TODO creare una classe sort

class Sort():
  def __init__(self, quit_event: Event, pause_event: Event) -> None:
    self.regex = RegexMedia()
    self.file = File()
    self.folder = Folder()
    self.file_error_logger = get_error_logger()
    self.quit_event = quit_event
    self.pause_event = pause_event
    self.tkinter_logger = get_tkinter_logger(Config.logs_obj)
    

  def start_sort(self) -> Union[bool, str]:
    result, msg = self.check_input_output_folders()
    if result == False: return result, msg
    try:
      Config.logs_obj.delete_logs()
      self.loop_into_folders()
      self.handle_folders_deletion()
      self.log_into_tkinter(
        self.tkinter_logger.debug,
        'sorting completed.')
      self.file.HASH_LIST.clear()
    except Exception:
      self.handle_exception()
      if not self.is_quit_set():
        Config.logs_obj.log_text_field.update_idletasks()
    return True, None

  @staticmethod
  def identify_media(file_path: str) -> Union[ImageHelper, VideoHelper, None]:
    """Identifica la classe di supporto per il tipo di media."""
    if ImageHelper.isImage(file_path):
        return ImageHelper()
    elif VideoHelper.isVideo(file_path):
        return VideoHelper()
    return None

  def handle_exception(self):
    """Gestisce le eccezioni durante l'elaborazione dei file."""
    self.file_error_logger.error('', exc_info=True)
    self.log_into_tkinter(self.tkinter_logger.error, 'An error occurred: file not sorted. See more information on error_logs.log')
    
  def get_date_path(self, date):
    if date[1] == None: 
      return join(Config.output_folder, date[0])
    elif date[2] == None: 
      return join(Config.output_folder, date[0], date[1])
    else: 
      return join(Config.output_folder, date[0], date[1], date[2])
  
  def check_input_output_folders(self):
    if(Config.input_folder == "" or Config.output_folder == "" or Config.input_folder == None or Config.output_folder == None):
      return False, "The source and destination folders cannot be empty"
    if(Config.input_folder == Config.output_folder):
      return False, "The source and destination folders cannot be the same"
    if Folder.path_is_parent(Config.input_folder, Config.output_folder) or Folder.path_is_parent(Config.output_folder, Config.input_folder):
      return False, "The source and destination folders cannot be one a subfolder of the other."
    if not listdir(Config.input_folder) :
      return False, "Start folder doesn't contain files. Process aborted."
    return True, None
    
  def is_quit_set(self):
    time.sleep(0.1)
    if self.quit_event and self.quit_event.is_set(): 
      return True
    return False
  
  def is_pause_set(self): return self.pause_event and self.pause_event.is_set()
  
  def log_into_tkinter(self, f, *args):
    if not self.is_quit_set():
      f(*args)
      Config.logs_obj.log_text_field.update_idletasks()
      
  def handle_folders_deletion(self):
    if self.is_quit_set(): return
    if(Config.get_checkbox_choises('DeleteEmptyFolders') and (not any(listdir(Config.input_folder)))):
      self.folder.delete_empty_folders(Config.input_folder)
      self.log_into_tkinter(
        self.tkinter_logger.info,
        'Empty folders deleted')
      
  def loop_into_folders(self):
    # ciclo tutte le cartelle
    for root, _, files in walk(Config.input_folder):
      root = root.replace('\\', '/')
      if self.is_quit_set(): return True
      self.folder_date = self.regex.extract_date_from_folder(root)
      self.loop_into_files(root, files)
      
  def loop_into_files(self, folder_path, file_list):
    for file_name in file_list:
      if self.is_quit_set(): return True
      if self.is_pause_set(): 
        self.pause_loop()
                  
      file_path = join(folder_path, file_name).replace('\\', '/')
      # se non è un immagine o un video, passa al file successivo
      media_class:VideoHelper|ImageHelper = Sort.identify_media(file_path)
      if media_class == None: continue
      
      if self.handle_duplicates(file_path, file_name):
        continue
      
      self.handle_move_file(media_class, file_path, file_name)
      
  def handle_duplicates(self, file_path, file_name):
    if self.file.isDuplicate(file_path): 
      if(Config.get_checkbox_choises('DeleteDuplicates')):
        remove(file_path)
        self.log_into_tkinter(
          self.tkinter_logger.info, 
          f'{file_name} - Duplicated detected: successfully deleted.')
      else:
        self.log_into_tkinter(
          self.tkinter_logger.inf, 
          f'{file_name} - Duplicated detected: file not moved.')
      return True
    return False
  
  def handle_move_file(self, media_class:VideoHelper|ImageHelper, file_path:str, file_name:str):
    date = media_class.extract_date(file_path, file_name, self.folder_date)
    
    # case no date found: file not moved
    if(date == None):
      self.log_into_tkinter(
        self.tkinter_logger.error, 
        f'{file_name} - No date found in the file: file not moved.')
      return
    
    # case date_found
    date_path = self.get_date_path(date)
    response = self.file.move_file(file_path, file_name, date_path)
    if response:
      self.log_into_tkinter(
        self.tkinter_logger.debug,
        f'{file_name} - moved successfully.')
    else: 
      self.log_into_tkinter(
        self.tkinter_logger.error,
        f'{file_name} - The file could not be moved')
      
  def pause_loop(self):
    self.log_into_tkinter(
      self.tkinter_logger.info, 
      "Sorting paused. Waiting for resume...")
    
    while self.is_pause_set():
      if(self.is_quit_set()): 
        return
      
    self.log_into_tkinter(
      self.tkinter_logger.info, 
      "Sorting resumed")