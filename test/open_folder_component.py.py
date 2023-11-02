import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Importa Pillow


def open_folder_dialog():
  folder_path = filedialog.askdirectory()
  if folder_path:
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder_path)

def resize_image(image_path, width, height):
  original_image = Image.open(image_path)
  resized_image = original_image.resize((width, height))
  return ImageTk.PhotoImage(resized_image)
  
root = tk.Tk()
root.title("Seleziona Cartella")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Cartella di input:")
label.grid(row=0, column=0)

path_entry = tk.Entry(frame)
path_entry.grid(row=0, column=1)

# Carica un'immagine per l'icona del pulsante
icon_image = resize_image("icon.ico", 13, 13)

browse_button = tk.Button(frame, image=icon_image, command=open_folder_dialog)
browse_button.grid(row=0, column=2)

# Assicurati che il PhotoImage non venga distrutto prematuramente
browse_button.image = icon_image

root.mainloop()
