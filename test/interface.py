from tkinter import Frame, Tk
from tkinter.ttk import Label, Button

from options import create_opt_frame
from folder_selection import create_selection_folder_frame
from logs import Logs

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
    create_selection_folder_frame(selection_folder_frame, self.icon_path)
    
    option_frame = Frame(form_frame)
    create_opt_frame(option_frame, self.default_font)
    option_frame.grid(row=0, column=1)
    
    btn = Button(root, text="Inizia", command=root.destroy)
    btn.pack()
    
    logs_frame = Frame(root)
    logs_frame.pack()
    logs = Logs(logs_frame)
    
    root.mainloop()
      
i = Interface("Sort Image", "800x800", "icon.ico", "Noto 10")