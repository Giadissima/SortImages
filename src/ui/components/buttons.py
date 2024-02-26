from typing import Callable
from src.files_manager.images import ImageHelper
from src.ui.settings.settings_style import main_color
from tkinter import Button
from tkinter.ttk import Frame

def create_rounded_button(father_frame:Frame, image_path:str, width:int, height:int, command:Callable=None):
  """This function is responsible for creating a button with a border-radius from a rounded image
  Args:
    father_frame (Frame): the folderthe frame on which to insert the button
    image_path (str): the rounded image path
    width (int): the width of the button
    height (int): the height of the button
    command (Callable, optional): function to call when the buttons is clicked. Defaults to None.

  Returns:
    Button|None: Button if created succesfully
  """
  image_resized = ImageHelper.resize_image(image_path, width, height)
  if image_resized:
    roundedbutton = Button(father_frame, fg='white', image=image_resized, command=command)
    roundedbutton.image = image_resized  # Save a reference to the image to avoid premature destruction
    roundedbutton["bg"] = main_color
    roundedbutton["border"] = "0"
    return roundedbutton
  else:
    print("Errore nel caricamento dell'immagine.")
    return None