from logging import Handler, LogRecord
from tkinter.scrolledtext import ScrolledText
from src.config.config import Config
class TkinterTextHandler(Handler):
  """Its functionality is to interface with the ScrolledText interface
  object and create a custom logger for the logging class."""
  def __init__(self, text_obj):
    super().__init__()
    self.text_obj:ScrolledText = text_obj

  def emit(self, record:LogRecord):
    msg = self.format(record)
    self.text_obj.add_logs(msg, record.levelname.lower())
    self.screen_flush()                                     
    
  def screen_flush(self):
    Config.logs_obj.log_text_field.update_idletasks()                                                                                         