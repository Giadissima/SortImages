import threading
import ctypes
class Mythread(threading.Thread): 
  
  # Target function for thread 
  def run(self): 
    for i in range(10000000): 
      print('Child Thread') 
          
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