import re

class RegexImage:
  def __init__(self):
    self.formats = { 
      # esempio di match: IMG_20221222_215022_388.jpg
      'whatsapp' : '^IMG_\d{8}_.{1,}',
      # esempio di match: IMG-20230206-WA0000.jpg
      'telegram' : '^IMG-\d{8}-.{1,}',
      # esempio di match: photo_2023-02-08_18-40-32.jpg
      'photo' : '^photo_\d{4}-\d{2}-\d{2}.{1,}',
      # Screenshot_20221212_182847.png
      'screen_shot' : '^Screenshot_\d{8}.{1,}',
    }

  def check_regex(self, text:str):
    """Controlla i vari formati della stringa text

    Args:
        text (str): il testo da matchare (il filename)

    Returns:
        None | [int, int, int]: Returns None if any formats match, otherwise it returns the date extrapolated
    """
    print(text)
    if re.search(self.formats['whatsapp'], text) or re.search(self.formats['telegram'], text):
      return [text[4:8], text[8:10], text[10:12]]
    elif re.search(self.formats['photo'], text):
      return [text[6:10], text[11:13], text[14:16]]
    elif re.search(self.formats['screen_shot'], text):
      return [text[11:15], text[15:17], text[17:19]]
    else: return None
    
class RegexVideo:
  pass