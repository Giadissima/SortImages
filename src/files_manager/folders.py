from os import listdir, rmdir
from os.path import abspath, commonpath, join, isdir
from pathlib import Path

from src.logs import get_error_logger


class Folder():
  def __init__(self, ):
    self.file_error_logger = get_error_logger()
  
  @staticmethod
  def path_is_parent(parent_path, child_path):
    parent_path = abspath(parent_path)
    child_path = abspath(child_path)

    # Compare the common path of the parent and child path with the common path of just 
    # the parent path. Using the commonpath method on just the parent path will regularise 
    # the path name in the same way as the comparison that deals with both paths, 
    # removing any trailing path separator
    return commonpath([parent_path]) == commonpath([parent_path, child_path])
  
  @staticmethod
  def create_nested_dir(path_to_create):
    Path(path_to_create).mkdir(parents=True, exist_ok=True)
    
  def delete_empty_folders(self, root):
    # se non è una cartella il percorso passato ritorno
    if not isdir(root): return
    
    # per ogni elemento nella cartella, controllo se è una directory, in caso affermativo, chiamo ricorsivamente la funzione
    for foldername in listdir(root):
      folderpath = join(root, foldername)
      if isdir(folderpath):
        self.delete_empty_folders(folderpath)

    # una volta rimosse le subdirs, controllo nuovamente se la cartella di partenza è vuota, se sì la cancello
    if not listdir(root):
      try:
        # Rimuovi la cartella vuota
        rmdir(root)
      except OSError as e:
        self.file_error_logger.error(f"non è stato possibile cancellare la cartella {root}, errore:\n{e}")