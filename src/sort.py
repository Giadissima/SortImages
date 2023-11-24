from os.path import join, basename
from src.folder import Folder
from src.config import Config
from src.regex import RegexMedia
from src.image import ImageHelper
from src.video import VideoHelper
from os import remove, rmdir, walk, listdir
from datetime import datetime
import traceback

regex = RegexMedia()
image = ImageHelper()
video = VideoHelper()

def extract_date(file_path, file, folder_date):
  if(folder_date != None and len(folder_date) == 3): 
    print(folder_date)
    print(file_path, "founded folder date")
    return folder_date
  if(image.isImage(file_path)): 
    date = image.get_date_from_metadata(file_path)
  else: 
    date = video.get_date_from_metadata(file_path)
  # se la data non era contenuta nei metadati allora guardo se la trovo nel nome del media
  if(date != None): return date 
  date = regex.extract_date_from_media(file, folder_date)
  return date

# TODO cosa succede se quitto mentre è in corso il processo?
def start_sort():
  # change this for selecting current image's path
  # config = Config()
  print(Config.checkbox_choises[0].get())
  if(Config.input_folder == "" or Config.output_folder == "" or Config.input_folder == None or Config.output_folder == None):
    return False, "The source and destination folders cannot be empty"
  if(Config.input_folder == Config.output_folder):
    return False, "The source and destination folders cannot be the same"
  if Folder.path_is_parent(Config.input_folder, Config.output_folder) or Folder.path_is_parent(Config.output_folder, Config.input_folder):
    return False, "The source and destination folders cannot be one a subfolder of the other."
  
  Config.logs_obj.delete_logs()
  # TODO il pulsante start deve diventare "pause"
  if not listdir(Config.input_folder) :
    return False, "Start folder doesn't contain files. Process aborted."
  
  # ciclo tutte le cartelle
  for root, dirs, files in walk(Config.input_folder):
    root = root.replace('\\', '/')
    folder_date = regex.extract_date_from_folder(root)
    # ciclo tutte le immagini
    for file in files:
      time = datetime.now()
      hour = time.hour
      minute = time.minute
      second = time.second
      try:
        file_path = join(root, file).replace('\\', '/')
        # se non è un immagine o un video, passa al file successivo
        if(not image.isImage(file_path) and not video.isVideo(file_path)): continue
        
        # se è un duplicato, lo cancello e passo all'immagine successiva
        if(image.isDuplicate(file_path)): 
          if(Config.checkbox_choises[0].get() == 1):
            remove(file_path)
            Config.logs_obj.add_logs(f'{hour}:{minute}:{second} {file_path} Duplicated detected: successfully deleted.', 'info')
          else:
            Config.logs_obj.add_logs(f'{hour}:{minute}:{second} {file_path} Duplicated detected: file not moved.', 'info')
          continue
        # TODO vedere se il timestamp cambia con più dati
        # TODO che succede se chiudo l'interfaccia mentre il progetto è attivo?
        date = extract_date(file_path, file, folder_date)
        if(date == None):
          Config.logs_obj.add_logs(f'{hour}:{minute}:{second} {file_path} No date found in the file: file not moved.', 'error')
        else:
          if(date[0] != None and date[1] == None): 
            date_path = join(Config.output_folder, date[0])
          elif date[0] != None and date[1] != None and date[2] == None: 
            date_path = join(Config.output_folder, date[0], date[1])
          else: 
            date_path = join(Config.output_folder, date[0], date[1], date[2])
          image.move_file(file_path, file, date_path)
          Config.logs_obj.add_logs(f'{hour}:{minute}:{second} {file_path} moved successfully.', 'default')
      except Exception as e:
        with open('error_logs.txt', 'a+') as file:
          file.write(f'{hour}:{minute}:{second}\nErrore: ')
          traceback.print_exc(file=file)
          file.write('\n')
        Config.logs_obj.add_logs(f'{file_path} An error occurred: file not sorted. See more information on error_logs.txt', 'error')
    if(Config.checkbox_choises[1].get() == 1 and (not any(listdir(root)))):
      rmdir(root)
      Config.logs_obj.add_logs(f'{hour}:{minute}:{second} {file_path} Empty folder deleted', 'info')
  Config.logs_obj.add_logs('sorting completed.', 'default')
  image.HASH_LIST = []
  return True, None