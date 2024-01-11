from threading import Semaphore

from meta.decorators import singleton

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