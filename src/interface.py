from tkinter import BOTH, Frame, Tk
from tkinter.ttk import Label, Button, Style

from src.sort import start_sort
from src.ui.options import create_opt_frame
from src.ui.folder_selection import create_selection_folder_frame
from src.ui.logs import Logs

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
    
    style = Style()

    Style().configure("TButton", padding=3, background="white")

    style.map("B.TButton",
    foreground=[('pressed', 'orange'), ('active', 'orange'), ('!pressed', 'red')],
    background=[('pressed', '!disabled', 'active', 'white')],
    font='Noto 10 bold'
    )
    
    title = Label(root, text=self.TITLE, font='Noto 16 bold', padding=10)
    title.pack()
    
    form_frame = Frame(root)
    form_frame.pack(expand=True, fill=BOTH)
    
    selection_folder_frame = Frame(form_frame)
    selection_folder_frame.grid(row=0, column=0, padx=10, sticky="nsew")
    create_selection_folder_frame(selection_folder_frame, self.icon_path, self.default_font)
    
    option_frame = Frame(form_frame)
    create_opt_frame(option_frame, self.default_font)
    option_frame.grid(row=0, column=1, sticky="nsew", padx=10)
    
    form_frame.columnconfigure(0, weight=1)  # Imposta il peso della colonna 0
    form_frame.columnconfigure(1, weight=1)  # Imposta il peso della colonna 1
    form_frame.rowconfigure(0, weight=1)     # Imposta il peso della riga 0
    
    btn = Button(root, text="Start", style="B.TButton", command=start_sort)
    btn.pack(pady=10)
    
    Logs(root)
    
    root.mainloop()