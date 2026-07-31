from threading import Event
from typing import Callable, Optional

class Pause():
  """Encapsulates the pause/resume state of a single sort run.

  Sort only ever calls wait_if_paused() between files; it doesn't need to
  know about threading.Event. CustomThread owns the instance and toggles
  it from the UI, optionally reacting to pause/resume via callbacks (e.g.
  to log a message)."""
  def __init__(self, on_pause: Optional[Callable[[], None]] = None, on_resume: Optional[Callable[[], None]] = None) -> None:
    self.event = Event()
    self.event.set() # not paused by default
    self.on_pause = on_pause
    self.on_resume = on_resume

  def pause(self)->None:
    """pause at the next wait_if_paused() call"""
    self.event.clear()

  def resume(self)->None:
    """resume a previously paused run"""
    self.event.set()

  def is_paused(self)->bool:
    return not self.event.is_set()

  def wait_if_paused(self)->None:
    """Blocks the caller while paused, checking periodically so a kill
    request can still interrupt it promptly."""
    if self.event.is_set(): return
    if self.on_pause: self.on_pause()
    while not self.event.wait(timeout=0.2):
      pass
    if self.on_resume: self.on_resume()
