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
  def get_date_from_metadata(img: str) -> Optional[List[str]]:
    """
    It takes an image and returns the acquisition date collected from its metadata

    Args:
      img (str): image's full path

    Returns:
      Optional[year(str), month(str), day(str)]: date extracted from image's metadata
    """
    try:
        with Image.open(img) as image:
            exifdata = image.getexif()
            print(exifdata)  # ti mostra tutti gli ID presenti

            # ID numerici EXIF in ordine di priorità
            date_tags_priority = [36867, 36868]  # DateTimeOriginal, DateTimeDigitized

            for tag_id in date_tags_priority:
                data = exifdata.get(tag_id)
                if not data:
                  continue

                if isinstance(data, bytes):
                  data = data.decode("utf-8", errors="ignore")
                

                # formato tipico 'YYYY:MM:DD HH:MM:SS'
                if isinstance(data, str) and len(data) >= 10 and data[4] == ":" and data[7] == ":":
                  year_part = data[0:4]
                  try:
                    yy = RegexManager.get_year(year_part)
                    mm = data[5:7]
                    dd = data[8:10]
                    if not yy:
                      continue
                    return [yy, mm, dd]
                  except ValueError:
                      continue  # metadato corrotto, passo al prossimo
            # se nessuno dei campi è stato trovato
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
    Recognized a photo by its extension.
    Args:
      img(str): name of the possibly image
    Returns:
      bool, True if file has an image extension, False otherwise"""
    img_extensions = {'jpg', 'jpeg', 'png', 'gif', 'icns', 'bmp', 'tiff', 'tif', 'webp', 'svg', 'eps', 'raw', 'ico', 'heif', 'bpg', 'jfif'}
    file_extension = img.rsplit('.',1)[1].lower()
    return file_extension in img_extensions