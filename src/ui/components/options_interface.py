from tkinter.ttk import Checkbutton, Frame, Label, Radiobutton
from tkinter import W, IntVar, StringVar

from src.config.config import Config
class OptionsFrame:
  """
  This class generates a frame containing the selection of
  options about sorting methods, duplicates management ecc
  """
  def __init__(self, frame):
    self.row = 0
    self.parent_frame = frame
    self.frame = Frame(self.parent_frame)
    self.choices = {}
    self.create_opt_frame()
    
  def create_opt_frame(self):
    """
    Creates a Frame containing checkboxes and radiobuttons
    that include all user-customized sorting options.
    """
    sub_title = Label(self.frame, text="Options", style="CardTitle.TLabel")
    sub_title.grid(row=0, sticky='w')

    self.set_generic_options()

    sub_title = Label(self.frame, text="Sorting Method", style="CardTitle.TLabel")
    sub_title.grid(row=self.row + 1, sticky='w')
    self.row += 2
    
    self.set_sorting_method()
    self.frame.pack(side='top')
    
  def set_generic_options(self):
    "set all checkboxes contains optional options"
    options = {
    "DeleteDuplicates": "Delete duplicate images and videos from folders",
    "DeleteEmptyFolders": "Delete empty folders after the sort process",
    "IgnoreFolderSort": "Do not consider the dates contained in the folders' name",
    "ScreenshotFolder": "Move all screenshots in a dedicated folder",
    "WhatsappFolder": "Don't move all Whatsapp media in a dedicated folder",
    "UnknownFolder": "Move all unrecognized files to a folder named 'Unknown'.",
    }

    # `row` is the index to keep track of which row of the grid you are in.
    # `enumerate(options)` returns a tuple with the key and text of the dictionary, which can then be stored as variables in parentheses.
    for self.row, (key, text) in enumerate(options.items(), start=1):
      self.choices[key] = IntVar()
      Checkbutton(self.frame, text=text, variable=self.choices[key]).grid(row=self.row, sticky=W)
    Config.set_checkbox_choises(self.choices)
    
  def set_sorting_method(self):
    "set radiobuttons contains sorting method. The default sorting method generate a path by year/month"
    sort_method = StringVar(value="YearMonth")
    sorting_method = {
    "YearMonthDay": "Moves images in 'year/month/day' folders path",
    "YearMonth": "Moves images in 'year/month' folders path",
    "Year": "Moves images in year folders",
    }
    Radiobutton(self.frame, text=sorting_method["YearMonthDay"], variable=sort_method, value="YearMonthDay").grid(row=self.row+1, sticky=W)
    Radiobutton(self.frame, text=sorting_method["YearMonth"], variable=sort_method, value="YearMonth").grid(row=self.row+2, sticky=W)
    Radiobutton(self.frame, text=sorting_method["Year"], variable=sort_method, value="Year").grid(row=self.row+3, sticky=W)
    self.row += 3
    Config.set_sort_method(sort_method)