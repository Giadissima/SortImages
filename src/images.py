from PIL import Image, UnidentifiedImageError
def isImage(img):
  try:
    image = Image.open(img)
    image.verify()
    return True
  except FileNotFoundError:
    raise FileNotFoundError("file non trovato")
  except UnidentifiedImageError:
    return False    
  except Exception:
    return False