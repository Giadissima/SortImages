from logging import Logger, FileHandler, ERROR, DEBUG, Formatter, getLogger

from meta.decorators import singleton
from src.logs.tkinter_logs import TkinterTextHandler
from src.thread.semaphore import SemaphoreManager
from src.ui.components.tkinter_logs import TkinterLogs

@singleton
class LogsHelper():
  def __init__(self, logs_obj):
    self.error_logger = self.get_error_logger()
    self.tkinter_logger = self.get_tkinter_logger(logs_obj)
    self.file_name:None|str = None
    self.semaphore = SemaphoreManager()
  
  def get_error_logger(self):
    """Create the error log stream from error file.

    Returns:
      Logger: The logger stream.
    """
    file_handler = FileHandler("error_logs.log")
    file_handler.setLevel(ERROR)
    file_handler.setFormatter(Formatter('%(asctime)s - %(levelname)s\n%(message)s'))
    file_logger = getLogger('file_logger')
    file_logger.addHandler(file_handler)
    
    return file_logger
    
  def get_tkinter_logger(self, logs_obj: TkinterLogs)->Logger:
    """Create the log stream from tkinter widget.

    Returns:
      Logger: The logger stream.
    """
    tkinter_text_handler = TkinterTextHandler(logs_obj)
    tkinter_text_handler.setFormatter(Formatter('%(asctime)s - %(message)s', '%H:%M:%S'))
    tkinter_text_handler.setLevel(DEBUG)
    tkinter_logger = getLogger('tkinter_logger')
    tkinter_logger.addHandler(tkinter_text_handler)
    tkinter_logger.setLevel(DEBUG)
    
    return tkinter_logger
  
  def log_tkinter(self, level:str, msg:str, file_name=True)->None:
    """allows you to log on the message widget by accessing it as a 
    sequential resource through the use of semaphores
    Args:
      level(str): log level. Different levels correspond to different colors displayed on the UI
      msg(str): message to display on the UI"""
    if self.semaphore.acquired: return
    if file_name: msg = f"{self.file_name} - " + msg
    self.semaphore.acquire()
    if(level=='debug'):
      self.tkinter_logger.debug(msg)
    elif(level=='info'):
      self.tkinter_logger.info(msg)
    elif(level=='warn'):
      self.tkinter_logger.warning(msg)
    elif(level=='error'):
      self.tkinter_logger.error(msg)
    self.semaphore.release()
    
  def log_traceback(self):
    """Shows the complete error that was throws and saves it to error.log"""
    self.error_logger.error('', exc_info=True)