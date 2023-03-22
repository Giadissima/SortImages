from os.path import join
from src.file_functions import move_file
from src.duplicates import isDuplicate
from src.images import get_date_from_metadata, isImage
from src.regex import Regex
from os import walk

def main():
  # change this for selecting current image's path
  current_path = "C:\\Users\\giada\\OneDrive\\Desktop\\current"
  # change this for selecting where move images
  new_path = "C:\\Users\\giada\\OneDrive\\Desktop\\new"
  DUPLICATED_PATH = join(new_path, "duplicated")
  UNKNOWN_PATH = join(new_path, "unknown")
  r = Regex()
  if(current_path == new_path): raise Exception("current path e new path non possono essere uguali!")
  # ciclo tutte le cartelle
  for root, dirs, files in walk(current_path):
    # ciclo tutte le immagini
    for file in files:
      file_path = join(root, file)
      # se non è un immagine, passa al file successivo
      if(not isImage(file_path)): continue
      # se è un duplicato, lo sposto nella cartella "duplicati" e passo all'immagine successiva
      if(isDuplicate(file_path)): 
        move_file(file_path, file, DUPLICATED_PATH)
        continue
      date = get_date_from_metadata(file_path)
      # se la data non era contenuta nei metadati allora guardo se la trovo nel nome dell'immagine
      if(date == None):
        date = r.check_regex(file)
      # se non l'ha ancora trovata la sposto nella cartella 'unknown'
      if(date == None):
        move_file(file_path, file, UNKNOWN_PATH)
      # se invece ha trovato la data la sposto nella cartella giusta
      else:
        date_path = join(new_path, date[0], date[1], date[2])
        move_file(file_path, file, date_path)

if __name__ == '__main__':
  main()