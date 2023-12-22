from tkinter import END, Button, Entry, Label, StringVar, filedialog
from src.files_manager.images import ImageHelper
from src.ui.utility.utility import configure_weight

class FolderSelection():
  def __init__(self, frame, folder_icon_path, font=None):
    self.frame = frame
    self.folder_icon_path = ImageHelper.resize_image(folder_icon_path, 13, 13)
    self.font = font
    self.folder_path_entries = {}
    self.create_widgets()

  def create_widgets(self):
    """ Creates buttons and labels necessary to interface"""
    self.create_folder_row(1, "Start folder:", "input_folder")
    self.create_folder_row(2, "Destination folder:", "output_folder")
    configure_weight(self.frame, [0, 1, 2], [1, 1, 1])

  def create_folder_row(self, row:int, label_text:str, entry_name:str):
    """Creates the row of the grid containing various components of the interface.

    Args:
      row (int): number of row that this function is generating
      label_text (str): Text of the label to be displayed on the screen.
      entry_name (str): Key in the dictionary of entries that contains their names.
    """
    label = Label(self.frame, text=label_text, font=self.font)
    label.grid(row=row, column=0, sticky='w')

    self.folder_path_entries[entry_name] = StringVar()
    path_entry = Entry(self.frame, font=self.font, textvariable=self.folder_path_entries[entry_name])
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