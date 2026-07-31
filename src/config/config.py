from typing import Dict, Union
from tkinter import IntVar, StringVar
from src.ui.components.tkinter_logs import TkinterLogs
import platform

class Config():
  """
  This class is used to store the information that the user has given in order to start
  organizing the images correctly. This information is what the user enters from the UI,
  for example, the input folder, output folder and checkboxes they have marked. This class
  does not "remember" the choices the user makes, unlike the ConfigManager class, whose
  usefulness is to save the most important information in a file
  """
  logs_obj: TkinterLogs = None
  input_folder: str = None
  output_folder: str = None
  os_system = platform.system()

  UI_OPTION_VARS: Dict[str, Union[IntVar, StringVar]] = {} # To store the actual tkinter variables

  UI_OPTIONS_DEFINITIONS = [
      {
          "group_label": "Sorting Method",
          "type": "radio",
          "config_key": "sort_method",
          "default": "YearMonth",
          "options": {
              "YearMonthDay": "Moves images in 'year/month/day' folders path",
              "YearMonth": "Moves images in 'year/month' folders path",
              "Year": "Moves images in year folders",
          }
      },
      {
          "group_label": "Metadata Priority",
          "type": "radio",
          "config_key": "images_metadata_priority",
          "default": "metadata",
          "options": {
              "metadata": "Prioritize image metadata over filename",
              "file_name": "Prioritize filename over image metadata"
          }
      },
      {
          "group_label": "Other Options",
          "type": "checkbox_group", # A group of checkboxes
          "options": [
              {"key": "DeleteDuplicates", "label": "Delete duplicate images", "default": False},
              {"key": "DeleteEmptyFolders", "label": "Delete empty folders", "default": False},
              {"key": "UnknownFolder", "label": "Create 'Unknown' folder if no date found", "default": False}, # This was an implicit option, making it explicit
              {"key": "ScreenshotFolder", "label": "Create 'Screenshot' folder", "default": False}, # Added this
              {"key": "WhatsappFolder", "label": "Create 'Whatsapp' folder", "default": False} # Added this
          ]
      },
      {
          "group_label": "Conflict Resolution",
          "type": "radio",
          "config_key": "conflict_resolution_method",
          "default": "rename",
          "options": {
              "overwrite": "Overwrite existing files",
              "rename": "Rename new file (e.g. file.1.jpg)",
              "skip": "Skip new file"
          }
      }
  ]

  # series of get and set that will be used to store and display information within the program
  @staticmethod
  def set_logs_obj(obj)->None: Config.logs_obj = obj
  @staticmethod
  def set_input_folder(path:str)->None: Config.input_folder = path
  @staticmethod
  def set_output_folder(path:str)->None: Config.output_folder = path
  
  @staticmethod
  def get_checkbox_choises(key:str)->bool: 
    if key in Config.UI_OPTION_VARS and isinstance(Config.UI_OPTION_VARS[key], IntVar):
      return Config.UI_OPTION_VARS[key].get() == 1
    return False # Default to False if option not found or not a checkbox

  @staticmethod
  def get_radio_choises(key:str)->str:
    if key in Config.UI_OPTION_VARS and isinstance(Config.UI_OPTION_VARS[key], StringVar):
      return Config.UI_OPTION_VARS[key].get()
    return "" # Default to empty string if option not found or not a radio