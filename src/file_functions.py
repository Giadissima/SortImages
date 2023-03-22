from os.path import join, exists
from os import rename
from pathlib import Path

def move_file(file_path: str, file_name: str, new_path: str):
  # print(current_path, file, new_path)
  create_nested_dir(new_path)
  # cambia il nome del file in modo univoco
  try:
    file_dest_path = join(new_path, file_name)
    i = 0
    file_list = file_name.rsplit('.', 1)
    while (exists(file_dest_path)):
      file_name = file_list[0] + "." + str(i) + "." + file_list[1]
      file_dest_path = join(new_path, file_name) 
      i+=1
    rename(file_path, join(new_path, file_name))
  except FileExistsError:
    print("file già esistente: ", file_name)
  except Exception:
    print("errore generico nello spostamento di ", file_name)

def create_nested_dir(path_to_create):
  Path(path_to_create).mkdir(parents=True, exist_ok=True)