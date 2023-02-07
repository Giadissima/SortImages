from os.path import join
from os import rename
from pathlib import Path

def move_file(current_path: str, file: str, new_path: str):
  create_nested_dir(new_path)
  try:
    rename(join(current_path, file), join(new_path, file))
  except FileExistsError:
    print("errore nello spostamento di ", file)

def create_nested_dir(path_to_create):
  Path(path_to_create).mkdir(parents=True, exist_ok=True)