from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS

def isImage(img):
  """return if file is an image and it can access on its

  Args:
      img (str): img path

  Returns:
      bool: True if is an image, otherwise False
  """
  try:
    with Image.open(img) as image:
      image.verify()
    return True
  except UnidentifiedImageError:
    return False
  
def get_date_from_metadata(img):
  """Prende un immagine e restituisce la data di creazione raccolta dai suoi metadati

  Args:
      img (str): full path dell'immagine

  Returns:
      data : data[0] = yy, data[1] = mm, data [2] = dd
      se non è riuscito a estrapolare la data, ritorna None
  """
  with Image.open(img) as image:
    exifdata = image.getexif()
    for tag_id in exifdata:
      # get the tag name, instead of human unreadable tag id
      tag = TAGS.get(tag_id, tag_id)
      data = exifdata.get(tag_id)
      # decode bytes 
      if isinstance(data, bytes):
          data = data.decode()
      # tipo data str e valore = 2023:01:31 13:19:34
      if(tag == 'DateTime'):
        yy = data[0:4]
        mm = data[5:7]
        dd = data[8:10]
        return [yy, mm, dd]
    return None