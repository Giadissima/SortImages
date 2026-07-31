from tkinter.ttk import Checkbutton, Frame, Label, Radiobutton
from tkinter import W, E, IntVar, StringVar

from src.config.config import Config
class OptionsFrame:
  """
  This class generates a frame containing the selection of
  options about sorting methods, duplicates management ecc
  """
  def __init__(self, frame):
    self.row = 0
    self.parent_frame = frame
    self.opt_main_container_frame = Frame(self.parent_frame)
    self.opt_main_container_frame.pack(fill="x", padx=10)

    self.left_opt_container_frame = Frame(self.opt_main_container_frame)
    self.left_opt_container_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

    self.right_opt_container_frame = Frame(self.opt_main_container_frame)
    self.right_opt_container_frame.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

    self.opt_main_container_frame.columnconfigure(0, weight=1)
    self.opt_main_container_frame.columnconfigure(1, weight=1)


    self.choices = {}
    self.create_left_opt_frame()
    self.create_right_opt_frame()
    
  def create_left_opt_frame(self):
    """
    Creates a Frame containing checkboxes and radiobuttons
    that include all user-customized sorting options.
    """
    sub_title = Label(self.left_opt_container_frame, text="Sorting Method", style="Title.TLabel")
    sub_title.grid(row=0, sticky='w')
    
    self.set_sorting_method()
    
  def create_right_opt_frame(self):
    row = 0
    sub_title = Label(self.right_opt_container_frame, text="Metadata Priority", style="Title.TLabel")
    sub_title.grid(row=row, sticky='w')

    self.set_metadata_priority_options(row)

  def set_sorting_method(self):
    "set radiobuttons contains sorting method. The default sorting method generate a path by year/month"
    sort_method = StringVar(value="YearMonth")
    sorting_method = {
    "YearMonthDay": "Moves images in 'year/month/day' folders path",
    "YearMonth": "Moves images in 'year/month' folders path",
    "Year": "Moves images in year folders",
    }
    Radiobutton(self.left_opt_container_frame, text=sorting_method["YearMonthDay"], variable=sort_method, value="YearMonthDay").grid(row=1, sticky=W)
    Radiobutton(self.left_opt_container_frame, text=sorting_method["YearMonth"], variable=sort_method, value="YearMonth").grid(row=2, sticky=W)
    Radiobutton(self.left_opt_container_frame, text=sorting_method["Year"], variable=sort_method, value="Year").grid(row=3, sticky=W)
    Config.set_sort_method(sort_method)

  def set_metadata_priority_options(self, row):
    "set radiobuttons contains images' metadata priority. The default metadata priority is to prioritize image metadata over filename"
    images_metadata_priority = StringVar(value="metadata")
    metadata_priority = {
    "metadata": "Prioritize image metadata over filename",
    "file_name": "Prioritize filename over image metadata"
    }
    Radiobutton(self.right_opt_container_frame, text=metadata_priority["metadata"], variable=images_metadata_priority, value="metadata").grid(row=row+1, sticky=W)
    Radiobutton(self.right_opt_container_frame, text=metadata_priority["file_name"], variable=images_metadata_priority, value="file_name").grid(row=row+2, sticky=W)
    row += 2
    Config.set_images_metadata_priority(images_metadata_priority)