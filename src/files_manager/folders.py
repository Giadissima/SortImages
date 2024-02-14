from os import listdir, rmdir, walk
from os.path import abspath, commonpath, join, isdir, exists, isdir
from pathlib import Path
from typing import Union

from src.sort.media_result_calculator import MediaResultCalculator
class Folder():
  def __init__(self):
    self.img_res_calc = MediaResultCalculator()
    
  @staticmethod
  def is_nested_dir(parent_path:str, child_path:str)->bool:
    """Check if child_path is actually a subdirectory of parent_path

    Args:
      parent_path (str): the folder we need to check if there is child_path inside it
      child_path (str): the folder we need to check if is subfolder of parent_path

    Returns:
      bool: true if child_path is a subfolder of parent_path, false otherwise"""
    parent_path = abspath(parent_path)
    child_path = abspath(child_path)
    return commonpath([parent_path]) == commonpath([parent_path, child_path])
  
  @staticmethod
  def create_nested_dir(path_to_create:str)->None:
    """If a path doesn't exist, create it

    Args:
      path_to_create (str): the path to create
    """
    Path(path_to_create).mkdir(parents=True, exist_ok=True)
    
  def delete_empty_folders(self, root:str)->None:
    """recursive function that loops into root folder to find subfolders and it deletes all empty folders

    Args:
      root (str): initial folder
    """
    self.img_res_calc.increment_total_folder_deleted()
    
    if root == None or not isdir(root): return None
    
    # For each item in the folder, check if it is a directory; if so, recursively call the function.
    for foldername in listdir(root):
      folderpath = join(root, foldername)
      if isdir(folderpath):
        self.delete_empty_folders(folderpath)

    # Once the subdirectories have been removed, check again if the original folder is empty; if it is, delete it.
    if not listdir(root):
      try:
        rmdir(root)
      except (OSError, PermissionError, IOError) as e:
        return f"The folder could not be deleted"
    return None
  
  @staticmethod
  def check_input_output_folders(input_folder, output_folder)->Union[bool, str]:
    """Check if the input and output folders are the same, 
    if the input folder is empty, 
    and if both are the same folder.
    
    Returns:
      Union[bool, str]: 
        bool: True if the process has completed without errors, False otherwise, 
        str: error's message, if the process has completed without errors, str will be None"""
    if(not Folder.if_folder_exists(input_folder) or not Folder.if_folder_exists(output_folder)):
      return False, "The source or destination folder doesn't not exists anymore"
    if(input_folder == "" or output_folder == "" or input_folder == None or output_folder == None):
      return False, "The source and destination folders cannot be empty"
    if(input_folder == output_folder):
      return False, "The source and destination folders cannot be the same"
    if Folder.is_nested_dir(output_folder, input_folder):
      return False, "The source folders cannot be a subfolder of the destination source"
    if not Folder.check_if_folder_contains_files(input_folder) :
      return False, "Start folder doesn't contain files. Process aborted."
    return True, None
  
  @staticmethod
  def if_folder_exists(folder_path:str)->bool:
    """Compare the common path of the parent and child path with the common path of just 
      the parent path

    folder_path (str): the folder we need to check if exists and if is a folder

    Returns:
      bool: true if folder exists, otherwise False"""
    return isdir(folder_path) and exists(folder_path)
  
  @staticmethod
  def check_if_folder_contains_files(path):
    for root, dirs, files in walk(path):
      for file in files:
        return True
    return False