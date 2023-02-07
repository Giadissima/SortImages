from os.path import join
from src.duplicates import isDuplicate
from src.images import isImage

def main():
  current_path = "C:\\Users\\giada\\OneDrive\\Desktop\\current"
  new_path = "C:\\Users\\giada\\OneDrive\\Desktop\\new"
  test_file = join(new_path, "1-1.jpg")
  print(isImage(test_file))

if __name__ == '__main__':
  main()