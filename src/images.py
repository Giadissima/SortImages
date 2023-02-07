from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS

def isImage(img):
  try:
    with Image.open(img) as image:
      image.verify()
    return True
  except UnidentifiedImageError:
    return False
  
def get_date_from_metadata(img):
  with Image.open(img) as image:
    exifdata = image.getexif()
    for tag_id in exifdata:
      # get the tag name, instead of human unreadable tag id
      tag = TAGS.get(tag_id, tag_id)
      data = exifdata.get(tag_id)
      # decode bytes 
      if isinstance(data, bytes):
          data = data.decode()
      if(tag == 'DateTime'):
        print(f"{tag:25}: {data}")