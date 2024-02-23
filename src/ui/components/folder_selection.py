from tkinter.ttk import Button, Frame, Entry, Label
from tkinter import END, StringVar, filedialog
from assets.load_img import INPUT_FOLDER_IMG_PATH, OUPUT_FOLDER_IMG_PATH
from src.config.config import Config
from src.files_manager.images import ImageHelper
from src.ui.utility.utility import configure_weight

class FolderSelection():
  """
  This class generates a frame containing the selection of input
  and output folders, along with hints regarding them.
  """
  def __init__(self, parent_frame, folder_icon_path):
    self.frame = Frame(parent_frame, style='Card.TFrame')
    self.folder_icon_path = ImageHelper.resize_image(folder_icon_path, 13, 13)
    self.input_folder_img = ImageHelper.resize_image(INPUT_FOLDER_IMG_PATH, 80,60)
    self.output_folder_img = ImageHelper.resize_image(OUPUT_FOLDER_IMG_PATH, 80,60)
    self.folder_path_entries = {}
    self.create_widgets()
    self.create_hints()

  def create_widgets(self):
    Label(self.frame, text="Select folders", style="CardTitle.TLabel").grid(row=0,column=0, sticky='we')
    """ Creates buttons and labels necessary to interface"""
    self.create_folder_row(1, "Start folder:", "input_folder")
    self.create_folder_row(2, "Destination folder:", "output_folder")
    configure_weight(self.frame, [0, 1, 2, 3], [1, 1, 1, 1])

  def create_folder_row(self, row:int, label_text:str, entry_name:str):
    """Creates the row of the grid containing various components of the interface.

    Args:
      row (int): number of row that this function is generating
      label_text (str): Text of the label to be displayed on the screen.
      entry_name (str): Key in the dictionary of entries that contains their names.
    """
    label = Label(self.frame, text=label_text)
    label.grid(row=row, column=0, sticky='w')

    self.folder_path_entries[entry_name] = StringVar()
    if Config.os_system == 'Windows': 
      path_entry = Entry(self.frame, textvariable=self.folder_path_entries[entry_name], width=40)
    else:
      path_entry = Entry(self.frame, textvariable=self.folder_path_entries[entry_name], width=20)
    path_entry.grid(row=row, column=1, pady=10, sticky='we')

    browse_button = Button(self.frame, image=self.folder_icon_path, command=lambda: self.open_folder_dialog(path_entry))
    browse_button.grid(row=row, column=2)
    browse_button.image = self.folder_icon_path

  def open_folder_dialog(self, entry:Entry):
    """Open a folder dialog to select a folder and save it to the entry parameter

    Args:
      entry (Entry): the Entry widget of tkinter to save the selected folder_path
    """
    folder_path = filedialog.askdirectory()
    if folder_path:
      entry.delete(0, END)
      entry.insert(0, folder_path)
      
  def create_hints(self):
    Label(self.frame, text="Hints", style="CardTitle.TLabel").grid(row=4,column=0, sticky='we')
    Label(self.frame, text="Start folder").grid(row=5,column=0, sticky='we')
    Label(self.frame, text="Destination folder").grid(row=5,column=1, sticky='we')
    Label(self.frame, image=self.input_folder_img).grid(row=6,column=0, sticky='we')
    Label(self.frame, image=self.output_folder_img).grid(row=6,column=1, sticky='we')
    