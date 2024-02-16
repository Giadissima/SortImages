import imghdr
from typing import List, Optional
from PIL import Image, UnidentifiedImageError
from PIL import ImageTk
from PIL.ExifTags import TAGS
from src.files_manager.files import File
from src.sort.regex.regex import RegexManager

class ImageHelper(File):
  def __init__(self):
    super().__init__()
    
  @staticmethod
  def isImage(img: str) -> bool:
    """ 
    Return True if the file is an image and can be accessed.

    Args:
      img (str): img path

    Returns:
      bool: True if is an image, otherwise False
    """
    try:
      with Image.open(img) as i:
        i.verify()
        return ImageHelper.is_image_by_extension(img)
    except (OSError, PermissionError, IOError):
      return False
    except Image.DecompressionBombError:
      return ImageHelper.is_image_by_extension(img)
    except UnidentifiedImageError:
      return False
    
  @staticmethod
  def get_date_from_metadata(img:str) -> Optional[List[str]]:
    """
    It takes an image and returns the creation date collected from its metadata

    Args:
      img (str): image's full path

    Returns:
      Optional[year(str), month(str), day(str)]: date extracted from image's metadata
    """
    try:
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
            yy = RegexManager.get_year(data[0:4])
            mm = data[5:7]
            dd = data[8:10]
            if not yy: return None
            return [yy, mm, dd]
        return None
    except (IOError, KeyError, AttributeError, UnicodeDecodeError):
      return None
    
  @staticmethod
  def resize_image(image_path:str, width:int, height:int)->Image:
    """resize image with specified size

    Args:
      image_path (str): image to resize
      width (int): new width of the image
      height (int): new height of the image

    Returns:
      Image: _description_
    """
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    return ImageTk.PhotoImage(resized_image)
  
  @staticmethod
  def is_image_by_extension(img):
    """
    Define an alternative way to recognized a photo by its extension.
    Args:
      img(str): name of the possibly image
    Returns:
      bool, True if file has an image extension, False otherwise"""
    img_extensions = {'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'webp', 'svg', 'eps', 'raw', 'ico', 'heif', 'bpg'}
    file_extension = img.rsplit('.',1)[1].lower()
    return file_extension in img_extensions