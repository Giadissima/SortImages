from tkinter import W, Checkbutton, Frame, IntVar, Label

from src.config.config import Config

class OptionsFrame:
  def __init__(self, frame, font=None):
    self.parent_frame = frame
    self.frame = Frame(self.parent_frame)
    self.font = font
    self.choices = {}
    self.create_opt_frame()

  def create_opt_frame(self):
    """Creates a Frame containing checkboxes that include all user-customized sorting options."""
    sub_title = Label(self.frame, text="Options", font='Noto 10 bold')
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
      Checkbutton(self.frame, text=text, variable=self.choices[key], font=self.font).grid(row=idx, sticky=W)

    Config.set_checkbox_choises(self.choices)