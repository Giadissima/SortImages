from os.path import join
from os import walk
from hashlib import md5

BUF_SIZE = 65536
HASH_LIST = []

def isDuplicate(file):
  """Find if file is a duplicate by the array contains al the hash previously seen

  Args:
      file (string): file to search duplicates
      path (string): path contains other files
  """
  file_hashed = hash_file(file)
  if file_hashed in HASH_LIST:
    return True
  HASH_LIST.append(file_hashed)
  return False
      
def hash_file(file):
  print(file)
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
    raise Exception ("errore nell'hashing del file") 