from tkinter import END, Button, Entry, Label, filedialog
from PIL import Image, ImageTk


def create_selection_folder_frame(frame, folder_icon_path):
    folder_icon_path = resize_image(folder_icon_path, 13, 13)
    
    # Cartella input field
    label_1 = Label(frame, text="Cartella di input:")
    label_1.grid(row=0, column=0)

    path_entry_1 = Entry(frame)
    path_entry_1.grid(row=0, column=1)
    
    browse_button_1 = Button(frame, image=folder_icon_path, command=lambda: open_folder_dialog(path_entry_1))
    browse_button_1.grid(row=0, column=2)
    browse_button_1.image = folder_icon_path
    
    # Cartella output field
    label_2 = Label(frame, text="Cartella di output:")
    label_2.grid(row=1, column=0)

    path_entry_2 = Entry(frame)
    path_entry_2.grid(row=1, column=1)
    
    browse_button_2 = Button(frame, image=folder_icon_path, command=lambda: open_folder_dialog(path_entry_2))
    browse_button_2.grid(row=1, column=2)
    browse_button_2.image = folder_icon_path
    
def resize_image(image_path, width, height):
  original_image = Image.open(image_path)
  resized_image = original_image.resize((width, height))
  return ImageTk.PhotoImage(resized_image)

def open_folder_dialog(entry):
  folder_path = filedialog.askdirectory()
  if folder_path:
    entry.delete(0, END)
    entry.insert(0, folder_path)