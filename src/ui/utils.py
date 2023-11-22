from PIL import Image, ImageTk

def resize_image(image_path, width, height):
  original_image = Image.open(image_path)
  resized_image = original_image.resize((width, height))
  return ImageTk.PhotoImage(resized_image)