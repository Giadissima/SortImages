from tkinter.ttk import Button
from tkinter import messagebox
from src.sort.sort import Sort
import threading
import ctypes
class CustomThread(threading.Thread):
  def __init__(self) -> None:
    super().__init__()
    self.sort_thread = None
    self.sort = Sort()
  
  def run(self, main_button:Button=None):
    """Starts the thread that will organize the files.

    Args:
      main_button (Button): The button inside the graphical interface whose text needs to be changed.
    
    Args:
        input_folder_entry (str): the text entry containing the input folder path
        text_entry2 (str): the text entry containing the output folder path
        check_and_set_preference (function): Check the saved user preferences.'
        main_button (Button): The button inside the graphical interface whose text needs to be changed.
    """
    
    # TODO disabilita il bottone finché non termina il thread
    
    result, msg = self.sort.start_sort()
    if result:
      messagebox.showinfo(title="Success", message="Sort completed")
    else:
      messagebox.showerror(title="Error", message=msg)
      
  def get_id(self):
    
    # returns id of the respective thread
    if hasattr(self, '_thread_id'):
      return self._thread_id
    for id, thread in threading._active.items():
      if thread is self:
        return id

  def kill(self):
    print("killing")
    thread_id = self.get_id()
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
      ctypes.py_object(SystemExit))
    if res > 1:
      ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
      print('Exception raise failure')