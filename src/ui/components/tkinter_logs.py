from tkinter import DISABLED, END, NORMAL, RIGHT, LEFT, BOTH
from tkinter.ttk import Frame
from tkinter.scrolledtext import ScrolledText
from src.ui.settings.settings_style import gray
class TkinterLogs():
  """
  This class is responsible for communicating with
  the widget that will serve as the Tkinter logger.
  """
  def __init__(self, frame: Frame):
    """Configure initial tags and the logs widget
    Args:
      frame (Frame): root frame where to pack the logs widget"""
    self.FRAME = frame

    self.log_text_field = ScrolledText(
      self.FRAME, state=DISABLED, height=13
    )

    self.log_text_field.config(bg=gray)
    self.log_text_field.tag_configure('error', foreground='red')
    self.log_text_field.tag_configure('info', foreground='light blue')
    self.log_text_field.tag_configure('debug', foreground='white')
    self.log_text_field.tag_configure('warning', foreground='orange')

    self.log_text_field.pack(fill='x', expand=True, padx=10, pady=10)

  def add_logs(self, message: str, tag: str):
    """Add a log into the logs widget on UI

    Args:
      message (str): message to write on the widget 
      tag (str): How to log the message and specify the logger level.
    """
    self.log_text_field.config(state=NORMAL)
    self.log_text_field.insert(END, f"{message}\n", tag)
    self.log_text_field.config(state=DISABLED)
    self.log_text_field.see(END)

  def delete_logs(self):
    """Delete logs on the widget"""
    self.log_text_field.config(state=NORMAL)
    self.log_text_field.delete(1.0, END)
    self.log_text_field.config(state=DISABLED)
