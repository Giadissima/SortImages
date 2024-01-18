import tkinter.ttk as ttk
import tkinter as tk
import os

from PIL import Image
from PIL import ImageTk

def create_card(title, card_height, card_width, side=None):
  card_container_frame = ttk.Frame(root)
  # card_container_frame.configure(bg=main_color)
  title = ttk.Label(card_container_frame, text=title, background=main_color, foreground='white')
  card_frame = ttk.Frame(card_container_frame, height=card_height, width=card_width)
  title.grid(column=0, row=0, sticky='w', padx=5)
  card_frame.grid(column=0, row=1, sticky='e')
  card_container_frame.pack(side=side)
  return card_frame

def resize_image(image_path:str, width:int, height:int):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    return ImageTk.PhotoImage(resized_image)
  
def create_rounded_button(image_path, width, height, command=None):
    image_resized = resize_image(image_path, width, height)
    if image_resized:
      roundedbutton = tk.Button(root, fg='white', image=image_resized, command=command)
      roundedbutton.image = image_resized  # Salva un riferimento all'immagine per evitarne la distruzione prematura
      roundedbutton["bg"] = main_color
      roundedbutton["border"] = "0"
      return roundedbutton
    else:
      # Aggiungi una gestione dell'errore nel caso l'immagine non venga caricata correttamente
      print("Errore nel caricamento dell'immagine.")
      return None
def configure_style():
  style = ttk.Style()
  
  # configure default styles
  style.configure("TCheckbutton", font=('Verdana', 11))
  style.configure("TLabel", font=('Verdana', 11))
  
  style.configure('TFrame', background=main_color)
  
  #subtitle style
  style.configure("Subtitle.TLabel", font=('Verdana', 15, 'bold'))
  
main_color = '#2A2A2A'
secondary_color = '#FF6B00'
# Initialize style
# Create style used by default for all Frames
#

root = tk.Tk()
root.title("Frame padre")
root.geometry("1600x900")
root.configure(bg=main_color)
style = configure_style()

title_img = resize_image('title.png', 344, 69)
title = ttk.Label(root, background=main_color, image=title_img)
title.image= title_img
subframe = ttk.Label(root, text='sub frame', background='green')
button = create_rounded_button('rounded_button.png', 230, 65, 'START')

title.pack(side='top', pady=(20,20))
subframe.pack(pady=20, fill='y', expand=True)
# log.pack(side='bottom',fill='x', ipady=100)
log_frame = create_card("Logs", 300, 1600, side='bottom')

button.pack(side='bottom', pady=(0, 20))



root.mainloop()


