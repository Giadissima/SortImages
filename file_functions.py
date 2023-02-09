from os.path import join
from os import rename
from pathlib import Path

def move_file(file_path: str, file_name: str, new_path: str):
  # print(current_path, file, new_path)
  create_nested_dir(new_path)
  try:
    rename(file_path, join(new_path, file_name))
  except FileExistsError:
    print("errore nello spostamento di ", file_name)

def create_nested_dir(path_to_create):
  Path(path_to_create).mkdir(parents=True, exist_ok=True)