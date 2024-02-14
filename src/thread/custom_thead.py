from tkinter.ttk import Button
from tkinter import messagebox
from src.sort.media_result_calculator import MediaResultCalculator
from src.sort.sort import Sort
import threading
import ctypes
from src.thread.semaphore import SemaphoreManager

class CustomThread(threading.Thread):
  def __init__(self, btn) -> None:
    super().__init__()
    self.sort_thread = None
    self.sort = Sort()
    self.btn:Button = btn
    self.semaphore = SemaphoreManager()
    self.img_res_calc = MediaResultCalculator()
  
  def run(self):
    """Starts the thread that will organize the files.

    Args:
      main_button (Button): The button inside the graphical interface whose text needs to be changed.
    
    Args:
        input_folder_entry (str): the text entry containing the input folder path
        text_entry2 (str): the text entry containing the output folder path
        check_and_set_preference (function): Check the saved user preferences.'
        main_button (Button): The button inside the graphical interface whose text needs to be changed.
    """
    
    self.btn.config(state="disabled")
    result, msg = self.sort.start_sort()
    if result:
      msg = f"""Sort completed.\n
Total media founded: {self.img_res_calc.TOTAL_IMG}
Total moved: {self.img_res_calc.TOTAL_IMG_MOVED}
Total without date: {self.img_res_calc.TOTAL_UNRECOGNIZED_IMG}
Total duplicates: {self.img_res_calc.TOTAL_MEDIA_DUPLICATES_FOUND}
Total deleted: {self.img_res_calc.TOTAL_IMG_DELETED}
Total folders deleted: {self.img_res_calc.TOTAL_FOLDER_DELETED}"""
      messagebox.showinfo(title="Success", message=msg)
    else:
      messagebox.showerror(title="Error", message=msg)
    self.btn.config(state="normal")
      
  def get_id(self):
    
    # returns id of the respective thread
    if hasattr(self, '_thread_id'):
      return self._thread_id
    for id, thread in threading._active.items():
      if thread is self:
        return id

  def kill(self):
    if self.semaphore: self.semaphore.wait_until_acquired()
    self.semaphore.wait_until_acquired()
    thread_id = self.get_id()
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
      ctypes.py_object(SystemExit))
    if res > 1:
      ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
      print('Exception raise failure')
    self.semaphore.release()