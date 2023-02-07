from os.path import join, realpath
from file_functions import create_nested_dir, move_file
from src.duplicates import isDuplicate
from src.images import get_date_from_metadata, isImage
from os import walk
def main():
  current_path = "C:\\Users\\giada\\OneDrive\\Desktop\\current"
  new_path = "C:\\Users\\giada\\OneDrive\\Desktop\\new"
  test_file = join(current_path, "wifi.jpg")
  for root, dirs, files in walk(current_path):
    for file in files:
      move_file(root, file, new_path)
      # print(isDuplicate(join(root, file)))
  # print(get_date_from_metadata(test_file))
  create_nested_dir(join(new_path, "a", "b"))

if __name__ == '__main__':
  main()