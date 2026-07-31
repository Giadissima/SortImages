from tkinter.ttk import Button
from tkinter import messagebox
from src.sort.media_result_calculator import MediaResultCalculator
from src.sort.sort import Sort
from src.thread.pause import Pause
from src.thread.stop import Stop
import threading
import ctypes
from src.thread.semaphore import SemaphoreManager

class CustomThread(threading.Thread):
  def __init__(self, btn, pause_btn=None) -> None:
    super().__init__()
    self.daemon = True # safety net: never let this thread block process exit
    self.sort_thread = None
    self.pause = Pause(on_pause=self._log_paused, on_resume=self._log_resumed)
    self.stop = Stop()
    self.sort = Sort(self.pause, self.stop)
    self.btn:Button = btn
    self.pause_btn:Button = pause_btn
    self.semaphore = SemaphoreManager()
    self.img_res_calc = MediaResultCalculator()

  def _log_paused(self)->None:
    logs = self.sort.logs
    if logs: logs.log_tkinter('info', 'Sorting paused. Waiting for resume...', file_name=False)

  def _log_resumed(self)->None:
    logs = self.sort.logs
    if logs: logs.log_tkinter('info', 'Sorting resumed', file_name=False)

  def run(self):
    """Starts the thread that will organize the files."""

    self.btn.config(state="disabled")
    if self.pause_btn: self.pause_btn.config(state="normal", text="Pause")
    result, msg = self.sort.start_sort()
    if self.stop.is_requested():
      return # the window is closing: don't touch UI that may already be gone
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
    if self.pause_btn: self.pause_btn.config(state="disabled", text="Pause")

  def get_id(self):
    """returns id of the respective thread"""
    if hasattr(self, '_thread_id'):
      return self._thread_id
    for id, thread in threading._active.items():
      if thread is self:
        return id

  def request_stop(self)->None:
    """Cooperatively ask the sort loop to stop. It will notice within the
    time of a single file operation and exit on its own - this is the
    reliable way to end it, unlike the forced kill() below."""
    self.pause.resume() # don't leave it stuck waiting to be resumed
    self.stop.request()

  def kill(self):
    """Force-kill as a last resort, only if request_stop() above wasn't
    acknowledged in time. Not reliable on its own: the injected exception
    is only delivered the next time this thread runs Python bytecode, so
    it can't interrupt a thread blocked in native code (image/video
    parsing, hashing, file I/O)."""
    if self.semaphore: self.semaphore.wait_until_acquired()
    thread_id = self.get_id()
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
      ctypes.py_object(SystemExit))
    if res > 1:
      ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
      print('Exception raise failure')
    self.semaphore.release()