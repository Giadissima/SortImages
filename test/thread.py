import threading
import ctypes
from s.s import SemaphoreManager
from time import sleep
class Mythread(threading.Thread): 
  # Target function for thread 
  def run(self): 
    self.s = SemaphoreManager()
    for i in range(10000000): 
      self.s.acquire()
      print('Child Thread')
      self.s.release() 
          
  def get_id(self):
  
    # returns id of the respective thread
    if hasattr(self, '_thread_id'):
      return self._thread_id
    for id, thread in threading._active.items():
      if thread is self:
        return id

  def kill(self):
    if self.s: self.s.wait_until_acquired()
    print("killing")
    thread_id = self.get_id()
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
      ctypes.py_object(SystemExit))
    if res > 1:
      ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
      print('Exception raise failure')
    self.s.release()