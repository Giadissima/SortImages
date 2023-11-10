from tkinter import END, W, Checkbutton, Entry, Frame, IntVar, Tk, filedialog
from tkinter.ttk import Label, Button
from PIL import Image, ImageTk

class Interface():
  def __init__(self, title: str, size: str, icon_path: str, default_font = None, default_font_size = None):
    self.TITLE = title
    self.SIZE = size
    self.icon_path = icon_path
    self.default_font = default_font
    self.default_font_size = default_font_size
    
    self.main_frame()
    
  def main_frame(self):
    root = Tk()
    root.title(self.TITLE)
    root.geometry(self.SIZE)
    root.iconbitmap(self.icon_path)
    
    title = Label(root, text=self.TITLE, font='Noto 14 bold', padding=10)
    title.pack()
    
    form_frame = Frame(root)
    form_frame.pack()
    
    selection_folder_frame = Frame(form_frame)
    selection_folder_frame.grid(row=0, column=0)
    self.create_selection_folder_frame(selection_folder_frame)
    
    option_frame = Frame(form_frame)
    self.create_opt_frame(option_frame)
    option_frame.grid(row=0, column=1)
    
    btn = Button(root, text="Inizia", command=root.destroy)
    btn.pack()
    
    logs_frame = Frame(root)
    logs_frame.pack()
    self.create_logs_frame(logs_frame)
    
    root.mainloop()
      
  def create_opt_frame(self, frame):
    options = [
      "Sposta file non identificati nella cartella \"Unknown\"",
      "Sposta file duplicati nella cartella \"Duplicates\"",
      "Cancella cartelle rimaste vuote",
      "Mantieni organizzazione parziale delle cartelle di input"
    ]

    choices = []
    
    for i in range(0, len(options)):
      choices.append(IntVar())
      Checkbutton(frame, text=options[i], variable=choices[-1], font=self.default_font).grid(row=i, sticky=W)
      
  def create_selection_folder_frame(self, frame, folder_icon_path = None):
    
    if(folder_icon_path is None): folder_icon_path = resize_image(self.icon_path, 13, 13)
    
    # Cartella input field
    label_1 = Label(frame, text="Cartella di input:")
    label_1.grid(row=0, column=0)

    path_entry_1 = Entry(frame)
    path_entry_1.grid(row=0, column=1)
    
    browse_button_1 = Button(frame, image=folder_icon_path, command=lambda: self.open_folder_dialog(path_entry_1))
    browse_button_1.grid(row=0, column=2)
    browse_button_1.image = folder_icon_path
    
    # Cartella output field
    label_2 = Label(frame, text="Cartella di output:")
    label_2.grid(row=1, column=0)

    path_entry_2 = Entry(frame)
    path_entry_2.grid(row=1, column=1)
    
    browse_button_2 = Button(frame, image=folder_icon_path, command=lambda: self.open_folder_dialog(path_entry_2))
    browse_button_2.grid(row=1, column=2)
    browse_button_2.image = folder_icon_path
    
  def open_folder_dialog(self, entry):
    folder_path = filedialog.askdirectory()
    if folder_path:
      entry.delete(0, END)
      entry.insert(0, folder_path)
      
  def create_logs_frame():

def resize_image(image_path, width, height):
  original_image = Image.open(image_path)
  resized_image = original_image.resize((width, height))
  return ImageTk.PhotoImage(resized_image)
      
i = Interface("Sort Image", "800x800", "icon.ico", "Noto 10")