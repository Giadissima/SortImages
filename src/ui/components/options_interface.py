from tkinter.ttk import Checkbutton, Frame, Label
from tkinter import W, IntVar

from src.config.config import Config
class OptionsFrame:
  def __init__(self, frame):
    self.parent_frame = frame
    self.frame = Frame(self.parent_frame, style='Card.TFrame')
    self.choices = {}
    self.create_opt_frame()
    
  def create_opt_frame(self):
    """Creates a Frame containing checkboxes that include all user-customized sorting options."""
    sub_title = Label(self.frame, text="Options", style="CardTitle.TLabel")
    sub_title.grid(row=0, sticky='w')

    options = {
      "DeleteDuplicates": "Delete duplicate images and videos from start folder",
      "DeleteEmptyFolders": "Delete empty folders after the sort process",
      "IgnoreFolderSort": "Do not consider folder names for sorting",
    }

    # `idx` is the index to keep track of which row of the grid you are in.
    # `enumerate(options)` returns a tuple with the key and text of the dictionary, which can then be stored as variables in parentheses.
    for idx, (key, text) in enumerate(options.items(), start=1):
      self.choices[key] = IntVar()
      Checkbutton(self.frame, text=text, variable=self.choices[key]).grid(row=idx, sticky=W)

    Config.set_checkbox_choises(self.choices)