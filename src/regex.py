import re

class Regex:
  formats = { 
    # esempio di match: IMG_20221222_215022_388.jpg
    'whatsapp' : '^IMG_\d{8}_.{1,}',
    # esempio di match: IMG-20230206-WA0000.jpg
    'telegram' : '^IMG-\d{8}-.{1,}',
    # esempio di match: photo_2023-02-08_18-40-32.jpg
    'photo' : '^photo_\d{4}-\d{2}-\d{2}.{1,}',
    # Screenshot_20221212_182847.png
    'screen_shot' : '/^Screenshot_\d{8}.{1,}',
  }
  def __init__(self):
    pass
  def check_regex(self, text:str):
    print(text)
    if re.search(Regex.formats['whatsapp'], text) or re.search(Regex.formats['telegram'], text):
      return [text[4:8], text[8:10], text[10:12]]
    elif re.search(Regex.formats['photo'], text):
      return [text[6:10], text[11:13], text[14:16]]
    elif re.search(Regex.formats['screen_shot'], text):
      print("\tmatch con screen_shot")
    else: return None