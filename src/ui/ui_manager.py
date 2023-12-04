from tkinter import BOTH, Frame, Label
from src.ui.components.options_interface import OptionsFrame
from src.ui.components.folder_selection import create_selection_folder_frame

class UIManager:
  def __init__(self, root, size, title, icon_path, default_font=None, default_font_size=None):
      self.root: Frame = root
      self.size = size
      self.title = title
      self.icon_path = icon_path
      self.default_font = default_font
      self.default_font_size = default_font_size

  def setup_ui(self):
    self.root.title(self.title)
    self.root.geometry(self.size)
    self.root.iconbitmap(self.icon_path)
    
    # TODO padding=10 non funziona più come parametro a label, capire perché
    title = Label(self.root, text="Image Sorter", font='Noto 16 bold')
    title.pack()
    
    form_frame = Frame(self.root)
    form_frame.pack(expand=True, fill=BOTH)

    selection_folder_frame = Frame(form_frame)
    selection_folder_frame.grid(row=0, column=0, padx=10, sticky="nsew")
    self.path_entry = create_selection_folder_frame(
        selection_folder_frame, self.icon_path, self.default_font)

    opt_frame = OptionsFrame(form_frame, self.default_font)
    opt_frame.frame.grid(row=0, column=1, sticky="nsew", padx=10)

    self.configure_tabel_weight(form_frame)
    
  def configure_tabel_weight(self, table: Frame, weight=1):
    table.columnconfigure(0, weight=weight)
    table.columnconfigure(1, weight=weight)
    table.rowconfigure(0, weight=weight)