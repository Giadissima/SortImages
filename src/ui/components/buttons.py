from src.files_manager.images import ImageHelper
from src.ui.settings.settings_style import main_color
from tkinter import Button

def create_rounded_button(father_frame, image_path, width, height, command=None):
    image_resized = ImageHelper.resize_image(image_path, width, height)
    if image_resized:
      roundedbutton = Button(father_frame, fg='white', image=image_resized, command=command)
      roundedbutton.image = image_resized  # Salva un riferimento all'immagine per evitarne la distruzione prematura
      roundedbutton["bg"] = main_color
      roundedbutton["border"] = "0"
      return roundedbutton
    else:
      # Aggiungi una gestione dell'errore nel caso l'immagine non venga caricata correttamente
      print("Errore nel caricamento dell'immagine.")
      return None