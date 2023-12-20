import logging
from tkinter.scrolledtext import ScrolledText
class TkinterTextHandler(logging.Handler):
  def __init__(self, text_obj):
    super().__init__()
    self.text_obj:ScrolledText = text_obj

  def emit(self, record):
    msg = self.format(record)
    self.text_obj.add_logs(msg, record.levelname.lower())