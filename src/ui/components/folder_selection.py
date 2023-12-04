from tkinter import END, Button, Entry, Label, filedialog
from src.files_manager.images import ImageHelper

# Todo ottimizzarla
def create_selection_folder_frame(frame, folder_icon_path, font=None):
    sub_title = Label(frame, text="Select Folders", font='Noto 10 bold')
    sub_title.grid(row=0, sticky='w')
    
    folder_icon_path = ImageHelper.resize_image(folder_icon_path, 13, 13)
    
    # Cartella input field
    label_1 = Label(frame, text="Start folder:", font=font)
    label_1.grid(row=1, column=0, sticky='w')

    path_entry_1 = Entry(frame, font=font)
    path_entry_1.grid(row=1, column=1, pady=10, sticky='we')
    
    browse_button_1 = Button(frame, image=folder_icon_path, command=lambda: open_folder_dialog(path_entry_1))
    browse_button_1.grid(row=1, column=2)
    browse_button_1.image = folder_icon_path
    
    # Cartella output field
    label_2 = Label(frame, text="Destination folder:", font=font)
    label_2.grid(row=2, column=0, sticky='w')

    path_entry_2 = Entry(frame, font=font)
    path_entry_2.grid(row=2, column=1, pady=10, sticky='we')
    
    browse_button_2 = Button(frame, image=folder_icon_path, command=lambda: open_folder_dialog(path_entry_2))
    browse_button_2.grid(row=2, column=2)
    browse_button_2.image = folder_icon_path
    
    frame.columnconfigure(1, weight=1)  # Imposta il peso della colonna 1
    frame.rowconfigure(1, weight=1)     # Imposta il peso della riga 0
    frame.rowconfigure(2, weight=1)     # Imposta il peso della riga 0
    return [path_entry_1, path_entry_2]

def open_folder_dialog(entry):
  folder_path = filedialog.askdirectory()
  if folder_path:
    entry.delete(0, END)
    entry.insert(0, folder_path)