from threading import Event

class Stop():
  """Cooperative cancellation signal for a running sort thread.

  Forcibly killing a Python thread (e.g. via ctypes async exceptions) can't
  reliably interrupt it while it's blocked in native code (image/video
  parsing, hashing, file I/O) - the exception is only delivered the next
  time the thread executes Python bytecode, which might take a while or
  never happen. Sort checks is_requested() between files instead, and
  exits on its own within the time of a single file operation."""
  def __init__(self) -> None:
    self.event = Event()

  def request(self)->None:
    self.event.set()

  def is_requested(self)->bool:
    return self.event.is_set()
