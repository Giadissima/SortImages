from typing import Dict
from tkinter import IntVar, StringVar
from src.logs.tkinter_logs import TkinterTextHandler
from src.ui.components.tkinter_logs import TkinterLogs

class Config():
  """
  This class is used to store the information that the user has given in order to start
  organizing the images correctly. This information is what the user enters from the UI,
  for example, the input folder, output folder and checkboxes they have marked. This class
  does not "remember" the choices the user makes, unlike the ConfigManager class, whose
  usefulness is to save the most important information in a file
  """
  logs_obj: TkinterLogs = None
  checkbox_choises = None
  input_folder: str = None
  output_folder: str = None
  sort_method: int = 0

  # series of get and set that will be used to store and display information within the program
  @staticmethod
  def set_logs_obj(obj: TkinterTextHandler)->None: Config.logs_obj = obj
  @staticmethod
  def set_input_folder(path:str)->None: Config.input_folder = path
  @staticmethod
  def set_output_folder(path:str)->None: Config.output_folder = path
  @staticmethod
  def set_checkbox_choises(arr: Dict[str, IntVar]): Config.checkbox_choises = arr
  @staticmethod
  def get_checkbox_choises(key:str)->bool: return Config.checkbox_choises[key].get() == 1
  @staticmethod
  def set_sort_method(var: StringVar)->None: Config.sort_method = var
  @staticmethod
  def get_sort_method(key:str)->bool: return Config.sort_method.get() == key