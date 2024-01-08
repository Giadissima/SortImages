from tkinter import BOTH
from tkinter.ttk import Frame, Label
from src.ui.components.options_interface import OptionsFrame
from src.ui.components.folder_selection import FolderSelection
from src.ui.utility.utility import configure_weight

class UIManager:
  def __init__(self, root: Frame, size, title, icon_path):
    self.root: Frame = root
    self.size = size
    self.title = title
    self.icon_path = icon_path

  def setup_ui(self):
    title = Label(self.root, text=self.title, style='Title.TLabel')
    title.pack()

    form_frame = Frame(self.root)
    form_frame.pack(expand=True, fill=BOTH)

    self.setup_main_frame()
    self.setup_selection_folder_frame(form_frame)
    self.setup_options_frame(form_frame)

    configure_weight(form_frame, [0], [0,1])

  def setup_selection_folder_frame(self, parent_frame):
    self.folder_selection_frame = FolderSelection(parent_frame, self.icon_path)
    self.folder_selection_frame.frame.grid(row=0, column=0, padx=10, sticky="nsew")
    
  def setup_options_frame(self, parent_frame):
    opt_frame = OptionsFrame(parent_frame)
    opt_frame.frame.grid(row=0, column=1, sticky="nsew", padx=10)

  def get_text_entries(self):
    input_folder = self.folder_selection_frame.folder_path_entries["input_folder"].get()
    output_folder = self.folder_selection_frame.folder_path_entries["output_folder"].get()
    return input_folder, output_folder
  
  def setup_main_frame(self):
    self.root.title(self.title)
    self.root.geometry(self.size)
    self.root.iconbitmap(self.icon_path)
