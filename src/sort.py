from os.path import join
from src.config import Config
from src.regex import RegexMedia
from src.image import ImageHelper
from src.video import VideoHelper
from os import walk

def start_sort():
  # change this for selecting current image's path
  # config = Config()
  # todo  VEDERE SE aggiungere o meno più caratteri strani nella regex
  # change this for selecting where move images
  DUPLICATED_PATH = join(Config.output_folder, "duplicated")
  UNKNOWN_PATH = join(Config.output_folder, "unknown")
  regex = RegexMedia()
  image = ImageHelper()
  video = VideoHelper()
  # TODO il controllo farlo in interface
  if(Config.input_folder == Config.output_folder): raise Exception("current path e new path non possono essere uguali!")
  # ciclo tutte le cartelle
  for root, dirs, files in walk(Config.input_folder):
    # ciclo tutte le immagini
    for file in files:
      file_path = join(root, file)
      # se non è un immagine, passa al file successivo
      if(not image.isImage(file_path) and not video.isVideo(file_path)): continue
      # se è un duplicato, lo sposto nella cartella "duplicati" e passo all'immagine successiva
      if(image.isDuplicate(file_path)): 
        image.move_file(file_path, file, DUPLICATED_PATH)
        continue
      # TODO elimina duplicati
      if(image.isImage(file_path)): 
        date = image.get_date_from_metadata(file_path)
      else: 
        date = video.get_date_from_metadata(file_path)
      # se la data non era contenuta nei metadati allora guardo se la trovo nel nome del media
      if(date == None):
        date = regex.check_regex(file)
      # se non l'ha ancora trovata la sposto nella cartella 'unknown'
      if(date == None):
      # TODO lascia doce stanno
        image.move_file(file_path, file, UNKNOWN_PATH)
      # se invece ha trovato la data la sposto nella cartella giusta
      else:
        date_path = join(Config.output_folder, date[0], date[1], date[2])
        image.move_file(file_path, file, date_path)