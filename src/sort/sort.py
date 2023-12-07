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
regex = RegexMedia()
file = File()
folder = Folder()
file_error_logger = get_error_logger()

def start_sort(pause_event: Event = None, quit_event: Event = None) -> Union[bool, str]:
  tkinter_logger = get_tkinter_logger(Config.logs_obj)
  
  if(Config.input_folder == "" or Config.output_folder == "" or Config.input_folder == None or Config.output_folder == None):
    return False, "The source and destination folders cannot be empty"
  if(Config.input_folder == Config.output_folder):
    return False, "The source and destination folders cannot be the same"
  if Folder.path_is_parent(Config.input_folder, Config.output_folder) or Folder.path_is_parent(Config.output_folder, Config.input_folder):
    return False, "The source and destination folders cannot be one a subfolder of the other."
  
  Config.logs_obj.delete_logs()
  if not listdir(Config.input_folder) :
    return False, "Start folder doesn't contain files. Process aborted."
  
  # ciclo tutte le cartelle
  for root, dirs, files in walk(Config.input_folder):
    root = root.replace('\\', '/')
    if(Config.get_checkbox_choises('IgnoreFolderSort')):
      folder_date = None
    else: folder_date = regex.extract_date_from_folder(root)
    # ciclo tutte le immagini
    for f in files:
      # print("a")
      if quit_event and quit_event.is_set(): 
        print("closing...")
        return True, None
      try:
        if pause_event and pause_event.is_set(): tkinter_logger.info("Sorting paused. Waiting for resume...")
        while pause_event and pause_event.is_set():
          if(has_thread_to_stop()): 
            return True, None
          print("aaaa")
          pause_event.wait()  # Attendi fino a quando l'Event viene cancellato
                    
        file_path = join(root, f).replace('\\', '/')
        # se non è un immagine o un video, passa al file successivo
        media_class:VideoHelper|ImageHelper = identify_media(file_path)
        if media_class == None: continue
        
        if(file.isDuplicate(file_path)): 
          if(Config.get_checkbox_choises('DeleteDuplicates')):
            remove(file_path)
            tkinter_logger.info(f'{f} - Duplicated detected: successfully deleted.')
          else:
            tkinter_logger.info(f'{f} - Duplicated detected: file not moved.')
          continue
        # print("b")
        date = media_class.extract_date(file_path, f, folder_date)
        # print("c")
        if(date == None):
          # print("f")
          tkinter_logger.error(f'{f} - No date found in the file: file not moved.')
          # print("g")
        else:
          # print("h")
          date_path = get_date_path(date)
          response = file.move_file(file_path, f, date_path)
          # print("i")
          if response and not has_thread_to_stop(quit_event):
            tkinter_logger.debug(f'{f} - moved successfully.')
            # print("error")
          else: 
            # print("m")
            if not has_thread_to_stop(quit_event):
              tkinter_logger.error(f'{f} - The file could not be moved')
        # print("d")
      except Exception:
        # print("e")
        handle_exception(tkinter_logger)
      finally: 
        if not has_thread_to_stop(quit_event): 
          Config.logs_obj.log_text_field.update_idletasks()
  if(Config.get_checkbox_choises('DeleteEmptyFolders') and (not any(listdir(root)))):
    folder.delete_empty_folders(Config.input_folder)
    tkinter_logger.info('Empty folders deleted')
  tkinter_logger.debug('sorting completed.')
  file.HASH_LIST.clear()
  return True, None

def identify_media(file_path: str) -> Union[ImageHelper, VideoHelper, None]:
  """Identifica la classe di supporto per il tipo di media."""
  if ImageHelper.isImage(file_path):
      return ImageHelper()
  elif VideoHelper.isVideo(file_path):
      return VideoHelper()
  return None

def handle_exception(tkinter_logger: Logger):
  """Gestisce le eccezioni durante l'elaborazione dei file."""
  file_error_logger.error('', exc_info=True)
  tkinter_logger.error('An error occurred: file not sorted. See more information on error_logs.log')
  
def get_date_path(date):
  if date[1] == None: 
    return join(Config.output_folder, date[0])
  elif date[2] == None: 
    return join(Config.output_folder, date[0], date[1])
  else: 
    return join(Config.output_folder, date[0], date[1], date[2])
  
def has_thread_to_stop(quit_event):
  time.sleep(0.1)
  if quit_event and quit_event.is_set(): 
    return True
  return False