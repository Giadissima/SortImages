from os.path import abspath, commonpath
from pathlib import Path


class Folder():
  def __init__(self, ):
    pass
  
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