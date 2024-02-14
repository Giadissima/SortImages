from typing import Callable
from src.config.config import Config
from src.thread.custom_thead import CustomThread
from tkinter.ttk import Button

class ThreadManager():
  def __init__(self) -> None:
    self.t:CustomThread = None
    
  # TODO vedere se funziona la tipizzazione
  def start_thread(self, input_folder_entry:str, output_folder_entry:str, check_and_set_preference: Callable, btn: Button)->None:
    """This function handles the start of the sorting thread and is responsible for
    displaying any message boxes containing buttons to click in order to save their
    preference in the config.ini file."""
    # controllo se il thread precedente è stato chiuso correttamente, se non è così esco
    if(self.t != None and self.t.is_alive()): return
    if(self.t != None):
      self.t = None
      
    msg1 = "The program will delete duplicate images and video.\nIt will not be possible to recover them.\nContinue?"
    msg2 = "Are you sure you want to delete empty folders\nfrom the starting folder?"

    if check_and_set_preference('DeleteDuplicates', msg1) == False: return
    if check_and_set_preference('DeleteEmptyFolders', msg2) == False: return

    Config.set_input_folder(input_folder_entry)
    Config.set_output_folder(output_folder_entry)
      
    self.t = CustomThread(btn)
    self.t.start()
    
  def kill_thread(self):
    """kill sorting thread"""
    if(self.t != None and self.t.is_alive()):
      self.t.kill()
      if(self.t.is_alive()):
        self.t.join(timeout=1)
      self.t = None