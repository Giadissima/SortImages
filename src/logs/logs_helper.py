import logging

from src.logs.tkinter_logs import TkinterTextHandler
from src.config.config import Config
from meta.decorators import singleton
from src.thread.semaphore import SemaphoreManager

@singleton
class LogsHelper():
  def __init__(self, logs_obj):
    self.error_logger = self.get_error_logger()
    self.tkinter_logger = self.get_tkinter_logger(logs_obj)
    self.semaphore = SemaphoreManager()
  
  def get_error_logger(self):
    """Create the error log stream from error file.

    Returns:
      Logger: The logger stream.
    """
    file_handler = logging.FileHandler("error_logs.log")
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s\n%(message)s'))
    file_logger = logging.getLogger('file_logger')
    file_logger.addHandler(file_handler)
    
    return file_logger
    
  def get_tkinter_logger(self, logs_obj):
    """Create the log stream from tkinter widget.

    Returns:
      Logger: The logger stream.
    """
    tkinter_text_handler = TkinterTextHandler(logs_obj)
    tkinter_text_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s', '%H:%M:%S'))
    tkinter_text_handler.setLevel(logging.DEBUG)
    tkinter_logger = logging.getLogger('tkinter_logger')
    tkinter_logger.addHandler(tkinter_text_handler)
    tkinter_logger.setLevel(logging.DEBUG)
    
    return tkinter_logger
  
  def log_tkinter(self, level, msg):
    if self.semaphore.acquired: return
    self.semaphore.acquire()
    if(level=='debug'):
      self.tkinter_logger.debug(msg)
    elif(level=='info'):
      self.tkinter_logger.info(msg)
    elif(level=='error'):
      self.tkinter_logger.error(msg)
        
    self.screen_flush()
    self.semaphore.release()
    
    
    # TODO controllrlo
  def log_traceback(self):
    print("error")
    self.error_logger.error('', exc_info=True)
  
  def screen_flush(self):
    Config.logs_obj.log_text_field.update_idletasks()