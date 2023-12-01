from os.path import join
from typing import Union
from src.folder import Folder
from src.config import Config
from src.regex import RegexMedia
from src.image import ImageHelper
from src.video import VideoHelper
from src.file import File
from os import remove, rmdir, walk, listdir
from datetime import datetime
import traceback

regex = RegexMedia()
file = File()

def start_sort() -> Union[bool, str]:
  # change this for selecting current image's path
  # config = Config()
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
    time = datetime.now()
    hour, minute, second = time.hour, time.minute, time.second
    root = root.replace('\\', '/')
    folder_date = regex.extract_date_from_folder(root)
    # ciclo tutte le immagini
    for f in files:
      time = datetime.now()
      hour, minute, second = time.hour, time.minute, time.second
      try:
        file_path = join(root, f).replace('\\', '/')
        # se non è un immagine o un video, passa al file successivo
        media_class:VideoHelper|ImageHelper = identify_media(file_path)
        if media_class == None: continue
        
        # se è un duplicato, lo cancello e passo all'immagine successiva
        if(file.isDuplicate(file_path)): 
          if(Config.checkbox_choises['DeleteDuplicates'].get() == 1):
            remove(file_path)
            Config.logs_obj.add_logs(f'{hour}:{minute}:{second} {file_path} Duplicated detected: successfully deleted.', 'info')
          else:
            Config.logs_obj.add_logs(f'{hour}:{minute}:{second} {file_path} Duplicated detected: file not moved.', 'info')
          continue
        date = media_class.extract_date(file_path, f, folder_date)
        if(date == None):
          Config.logs_obj.add_logs(f'{hour}:{minute}:{second} {file_path} No date found in the file: file not moved.', 'error')
        else: # TODO farlo in una funzione
          if(date[0] != None and date[1] == None): 
            date_path = join(Config.output_folder, date[0])
          elif date[0] != None and date[1] != None and date[2] == None: 
            date_path = join(Config.output_folder, date[0], date[1])
          else: 
            date_path = join(Config.output_folder, date[0], date[1], date[2])
          file.move_file(file_path, f, date_path)
          Config.logs_obj.add_logs(f'{hour}:{minute}:{second} {file_path} moved successfully.', 'default')
      except Exception as e:
        handle_exception(file_path, e)
      finally: Config.logs_obj.log_text_field.update_idletasks()
    if(Config.checkbox_choises['DeleteEmptyFolders'].get() == 1 and (not any(listdir(root)))):
      rmdir(root)
      Config.logs_obj.add_logs(f'{hour}:{minute}:{second} {file_path} Empty folder deleted', 'info')
  Config.logs_obj.add_logs('sorting completed.', 'default')
  file.HASH_LIST.clear()
  return True, None

def identify_media(file_path: str) -> Union[ImageHelper, VideoHelper, None]:
  """Identifica la classe di supporto per il tipo di media."""
  if ImageHelper.isImage(file_path):
      return ImageHelper()
  elif VideoHelper.isVideo(file_path):
      return VideoHelper()
  return None

def handle_exception(file_path: str, exception: Exception):
  """Gestisce le eccezioni durante l'elaborazione dei file."""
  time = datetime.now()
  hour, minute, second = time.hour, time.minute, time.second
  with open('error_logs.txt', 'a+') as f:
      f.write(f'{hour}:{minute}:{second}\nErrore: ')
      traceback.print_exc(file=f)
      f.write('\n')
  Config.logs_obj.add_logs(f'{file_path} An error occurred: file not sorted. '
                            f'See more information on error_logs.txt', 'error')