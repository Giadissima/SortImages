from hashlib import md5
from os.path import join, exists
from os import rename
from pathlib import Path
# from hashlib import md5s

class File:
  def __init__(self):
    self.BUF_SIZE = 65536
    self.HASH_LIST = []
    
  def create_nested_dir(self, path_to_create):
    Path(path_to_create).mkdir(parents=True, exist_ok=True)
    
  def move_file(self, file_path: str, file_name: str, new_path: str):
    # print(current_path, file, new_path)
    self.create_nested_dir(new_path)
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
    except Exception as e:
      print(f"errore generico nello spostamento di {file_name}: \n{e}")
      
  def isDuplicate(self, file):
    """Find if file is a duplicate by the array contains al the hash previously seen

    Args:
        file (string): file to search duplicates
        path (string): path contains other files
    """ 
    file_hashed = self.hash_file(file)
    if file_hashed in self.HASH_LIST:
      return True
    self.HASH_LIST.append(file_hashed)
    return False
      
  def hash_file(self, file):
    # print(file)
    hash = md5()
    try:
      with open(file, 'rb') as f:
        while True:
          data = f.read(self.BUF_SIZE)
          if not data:
              break
          hash.update(data)
      return hash.hexdigest()
    except:
      raise Exception ("errore nell'hashing del file") 
