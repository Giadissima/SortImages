from tkinter.ttk import Checkbutton, Frame, Label, Radiobutton
from tkinter import W, E, IntVar, StringVar
from textwrap import fill

from src.config.config import Config

WRAP_WIDTH = 30 # characters, ttk Radiobutton/Checkbutton have no wraplength option

class OptionsFrame:
  """
  This class generates a frame containing the selection of
  options about sorting methods, duplicates management ecc
  """
  def __init__(self, frame):
    self.parent_frame = frame
    self.opt_main_container_frame = Frame(self.parent_frame)
    self.opt_main_container_frame.pack(fill="x", padx=10)

    self.left_opt_container_frame = Frame(self.opt_main_container_frame)
    self.left_opt_container_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

    self.right_opt_container_frame = Frame(self.opt_main_container_frame)
    self.right_opt_container_frame.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

    self.opt_main_container_frame.columnconfigure(0, weight=1)
    self.opt_main_container_frame.columnconfigure(1, weight=1)

    self.current_row_left = 0
    self.current_row_right = 0
    self.create_dynamic_options()
    
  def create_dynamic_options(self):
    right_column_groups = ["Metadata Priority", "Conflict Resolution"]
    for option_group in Config.UI_OPTIONS_DEFINITIONS:
      group_label = option_group["group_label"]
      option_type = option_group["type"]

      if group_label in right_column_groups: # Place Metadata Priority and Conflict Resolution on the right side
        container_frame = self.right_opt_container_frame
        current_row_attr = "current_row_right"
      else: # Place others on the left side
        container_frame = self.left_opt_container_frame
        current_row_attr = "current_row_left"

      # Add group label
      if getattr(self, current_row_attr) > 0: # Add padding if not the first group
        setattr(self, current_row_attr, getattr(self, current_row_attr) + 1) # Add a row for padding
      
      Label(container_frame, text=group_label, style="Title.TLabel").grid(row=getattr(self, current_row_attr), sticky=W)
      setattr(self, current_row_attr, getattr(self, current_row_attr) + 1)
      
      if option_type == "radio":
        config_key = option_group["config_key"]
        default_value = option_group["default"]
        options = option_group["options"]

        var = StringVar(value=default_value)
        Config.UI_OPTION_VARS[config_key] = var

        for value, text in options.items():
          Radiobutton(container_frame, text=fill(text, WRAP_WIDTH), variable=var,
                      value=value).grid(row=getattr(self, current_row_attr), sticky=W)
          setattr(self, current_row_attr, getattr(self, current_row_attr) + 1)

      elif option_type == "checkbox_group":
        for checkbox_def in option_group["options"]:
          key = checkbox_def["key"]
          label = checkbox_def["label"]
          default = checkbox_def["default"]

          var = IntVar(value=1 if default else 0)
          Config.UI_OPTION_VARS[key] = var

          Checkbutton(container_frame, text=fill(label, WRAP_WIDTH), variable=var).grid(
                      row=getattr(self, current_row_attr), sticky=W)
          setattr(self, current_row_attr, getattr(self, current_row_attr) + 1)