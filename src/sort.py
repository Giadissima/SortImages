from os.path import join
from src.config import Config
from src.regex import RegexMedia
from src.image import ImageHelper
from src.video import VideoHelper
from src.file import File
from os import walk


def start_sort():
  # change this for selecting current image's path
  # config = Config()
  # todo  VEDERE SE aggiungere o meno più caratteri strani nella regex
  regex = RegexMedia()
  image = ImageHelper()
  video = VideoHelper()

  print(Config.input_folder)
  if(Config.input_folder == "" or Config.output_folder == "" or Config.input_folder == None or Config.output_folder == None):
    return False, "The source and destination folders cannot be empty"
  if(Config.input_folder == Config.output_folder):
    return False, "The source and destination folders cannot be the same"
  if File.path_is_parent(Config.input_folder, Config.output_folder) or File.path_is_parent(Config.output_folder, Config.input_folder):
    return False, "The source and destination folders cannot be one a subfolder of the other."
  
  Config.logs_obj.delete_logs()
  # TODO il pulsante start deve diventare "pause"
  # TODO fre un messaggio in cui si avverte che la cartella di partenza è vuota e non cancellare i log e non stampare "sorting completed"
  # ciclo tutte le cartelle
  for root, dirs, files in walk(Config.input_folder):
    # ciclo tutte le immagini
    for file in files:
      try:
        file_path = join(root, file).replace('\\', '/')
        # se non è un immagine, passa al file successivo
        if(not image.isImage(file_path) and not video.isVideo(file_path)): continue
        # se è un duplicato, lo sposto nella cartella "duplicati" e passo all'immagine successiva
        if(image.isDuplicate(file_path)): 
          # TODO rimuoverlo
          # remove(file_path)
          Config.logs_obj.add_logs(f'{file_path} Duplicated detected: successfully deleted.', 'info')
          continue
        if(image.isImage(file_path)): 
          date = image.get_date_from_metadata(file_path)
        else: 
          date = video.get_date_from_metadata(file_path)
        # se la data non era contenuta nei metadati allora guardo se la trovo nel nome del media
        if(date == None):
          date = regex.check_regex(file)
        # se non l'ha ancora trovata la sposto nella cartella 'unknown'
        if(date == None):
          Config.logs_obj.add_logs(f'{file_path} No date found in the file: file not moved.', 'error')
        else:
          date_path = join(Config.output_folder, date[0], date[1], date[2])
          image.move_file(file_path, file, date_path)
          Config.logs_obj.add_logs(f'{file_path} moved successfully.', 'default')
      except Exception as e:
        with open('error_logs.txt', 'a+') as file:
          file.write(str(e) + '\n')
        Config.logs_obj.add_logs(f'{file_path} An error occurred: file not sorted. See more information on error_logs.txt', 'error')
  Config.logs_obj.add_logs('sorting completed.', 'default')
  return True, None
  
