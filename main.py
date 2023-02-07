from os.path import join
from src.duplicates import isDuplicate
from src.images import extract_metadata, isImage

def main():
  current_path = "C:\\Users\\giada\\OneDrive\\Desktop\\current"
  new_path = "C:\\Users\\giada\\OneDrive\\Desktop\\new"
  test_file = join(current_path, "wifi.jpg")
  print(extract_metadata(test_file))

if __name__ == '__main__':
  main()