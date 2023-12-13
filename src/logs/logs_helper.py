import logging

from src.logs.tkinter_logs import TkinterTextHandler

class LogsHelper():
  def __init__(self, logs_obj):
    self.error_logger = self.get_error_logger()
    self.tkinter_logger = self.get_tkinter_logger(logs_obj)
  
  def get_error_logger(self):
    file_logger = logging.getLogger('file_logger')
    # Configura l'handler per il file di log
    file_handler = logging.FileHandler("error_logs.log")
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s\n%(message)s'))
    file_logger.addHandler(file_handler)
    
    return file_logger
    
  def get_tkinter_logger(self, logs_obj):
    tkinter_logger = logging.getLogger('tkinter_logger')
    # Configura l'handler per il widget Text di Tkinter
    tkinter_text_handler = TkinterTextHandler(logs_obj)
    tkinter_text_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s', '%H:%M:%S'))
    tkinter_text_handler.setLevel(logging.DEBUG)
    tkinter_logger.addHandler(tkinter_text_handler)
    tkinter_logger.setLevel(logging.DEBUG)
    
    return tkinter_logger