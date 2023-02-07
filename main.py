from os.path import join
from src.duplicati import isDuplicate

def main():
  current_path = "C:\\Users\\giada\\OneDrive\\Desktop\\current"
  new_path = "C:\\Users\\giada\\OneDrive\\Desktop\\new"
  test_file = join(current_path, "photo_2023-02-07_09-26-15.jpg")
  print(isDuplicate(test_file, new_path))

if __name__ == '__main__':
  main()