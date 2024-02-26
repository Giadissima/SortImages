from threading import Semaphore

from meta.decorators import singleton

"""This class is a singleton wrapper of the threading.Semaphore library.
It adds a boolean that indicates whether the semaphore is green or red,
and a function that waits until the semaphore turns green."""
@singleton
class SemaphoreManager():
  def __init__(self):
    self.semaphore = Semaphore()
    self.acquired = False
  
  def acquire(self):
    if self.acquired: return
    self.semaphore.acquire()
    self.acquired = True
  
  def release(self):
    if not self.acquired: return
    self.acquired = False
    self.semaphore.release()
  
  def wait_until_acquired(self):
    self.semaphore.acquire(timeout=1)
    self.acquired=True