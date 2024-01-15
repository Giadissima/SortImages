from threading import Semaphore

from meta.decorators import singleton

@singleton
class SemaphoreManager():
  def __init__(self):
    self.semaphore = Semaphore()
    self.acquired = False
  
  def acquire(self):
    print("acquiring...", self.acquired)
    if self.acquired: return
    self.semaphore.acquire()
    self.acquired = True
    print("acquired...", self.acquired)
    
  
  def release(self):
    print("releasing", self.acquired)
    if not self.acquired: return
    self.acquired = False
    self.semaphore.release()
    print("released", self.acquired)
    
  def wait_until_acquired(self):
    self.semaphore.acquire()
    self.acquired = True