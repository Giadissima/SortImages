from threading import Semaphore

from meta.decorators import singleton

@singleton
class SemaphoreManager():
  def __init__(self) -> None:
    self.semaphore = Semaphore()
    self.acquired = False
  
  def acquire(self):
    self.acquired = self.semaphore.acquire()
  
  def release(self):
    self.acquired = False
    self.semaphore.release()
  
  def wait_until_semaphore_released(self):
    while not self.acquire(): pass