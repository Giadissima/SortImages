import re

class Regex:
  formats = { 
    'whatsapp' : '^IMG_\d{8}_.{1,}',
    'telegram' : '^IMG-\d{8}-.{1,}',
    'gallery1' : '',
    'gallery2' : ''
  }
  def __init__(self):
    pass
  def check_regex(self, text:str):
    print(text)
    if re.search(Regex.formats['whatsapp'], text):
      print("\tmatch con whatsapp")