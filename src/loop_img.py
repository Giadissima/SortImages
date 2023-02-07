from os import walk
def loop_img(path):
  for root, dirs, files in walk(path):
    for file in files:
      pass