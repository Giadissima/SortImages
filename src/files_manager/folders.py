from os import listdir, rmdir
from os.path import abspath, commonpath, join, isdir
from pathlib import Path
from typing import Union
class Folder():
  
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
    if root == None or not isdir(root): return
    
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
        return f"non è stato possibile cancellare la cartella {root}, errore:\n{e}"
    return None
  
  @staticmethod
  def check_input_output_folders(input_folder, output_folder)->Union[bool, str]:
    """Check if the input and output folders are the same, 
    if the input folder is empty, 
    and if the same folder has been passed twice.
    
    Returns:
      Union[bool, str]: 
        bool: True if the process has completed without errors, False otherwise, 
        str: error's message, if the pricess has completed without errors, str will be None"""
    if(input_folder == "" or output_folder == "" or input_folder == None or output_folder == None):
      return False, "The source and destination folders cannot be empty"
    if(input_folder == output_folder):
      return False, "The source and destination folders cannot be the same"
    if Folder.path_is_parent(input_folder, output_folder) or Folder.path_is_parent(output_folder, input_folder):
      return False, "The source and destination folders cannot be one a subfolder of the other."
    if not listdir(input_folder) :
      return False, "Start folder doesn't contain files. Process aborted."
    return True, None