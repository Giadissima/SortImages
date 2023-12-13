from threading import Event
from time import sleep
class ThreadEventsManager():
  def __init__(self, quit_event: Event, pause_event: Event) -> None:
    self.quit_event = quit_event
    self.pause_event = pause_event
  
  def pause_loop(self):
    """Creates a loop in which the thread simply waits without performing operations,
    and it ends when the process is not resumed."""
    
    while self.is_pause_set():
      if(self.is_quit_set()): 
        return
    
  def is_quit_set(self):
    """return true if quit event is set, false otherwise"""
    sleep(0.1)
    if self.quit_event and self.quit_event.is_set(): 
      return True
    return False
  
  def is_pause_set(self): 
    """return true if pause event is set, false otherwise"""
    return self.pause_event and self.pause_event.is_set()