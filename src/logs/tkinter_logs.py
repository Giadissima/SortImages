import logging

class TkinterTextHandler(logging.Handler):
  def __init__(self, text_obj):
    super().__init__()
    self.text_obj = text_obj

  def emit(self, record):
    msg = self.format(record)
    self.text_obj.add_logs(msg, record.levelname.lower())