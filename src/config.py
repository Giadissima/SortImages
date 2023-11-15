from src.ui.log import Logs

class Config():
  logs_obj: Logs = None
  checkbox_choises = None
  input_folder: str = None
  output_folder: str = None

  def set_logs_obj(self, obj): Config.logs_obj = obj
  def set_input_folder(self, path): Config.input_folder = path
  def set_output_folder(self, path): Config.output_folder = path
  def set_checkbox_choises(self, arr): Config.checkbox_choises = arr