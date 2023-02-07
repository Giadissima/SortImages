from os.path import join
from os import walk
from hashlib import md5

BUF_SIZE = 65536

def isDuplicate(file, path):
  """Find if file is a duplicate on the specified path

  Args:
      file (string): file to search duplicates
      path (string): path contains other files
  """
  file_hashed = hash_file(file)
  for root, dirs, other_files in walk(path):
    for other_file in other_files:
      other_file_hash = hash_file(join(path, other_file))
      if file_hashed == other_file_hash: 
        return True
  return False
      
def hash_file(file):
  hash = md5()
  try:
    with open(file, 'rb') as f:
      while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        hash.update(data)
    return hash.hexdigest()
  except:
    raise Exception (f"errore nell'hashing di {file}")
  