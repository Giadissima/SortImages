from PIL import Image, UnidentifiedImageError
def isImage(img):
  try:
    with Image.open(img) as image:
      image.verify()
    return True
  except UnidentifiedImageError:
    return False