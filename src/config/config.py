from src.ui.components.tkinter_logs import TkinterLogs

class Config():
  logs_obj: TkinterLogs = None
  checkbox_choises = None
  input_folder: str = None
  output_folder: str = None
  sort_method: int = 0

  @staticmethod
  def set_logs_obj(obj): Config.logs_obj = obj
  @staticmethod
  def set_input_folder(path): Config.input_folder = path
  @staticmethod
  def set_output_folder(path): Config.output_folder = path
  @staticmethod
  def set_checkbox_choises(arr): Config.checkbox_choises = arr
  @staticmethod
  def get_checkbox_choises(key)->bool: 
    return Config.checkbox_choises[key].get() == 1
  @staticmethod
  def set_sort_method(var): Config.sort_method = var