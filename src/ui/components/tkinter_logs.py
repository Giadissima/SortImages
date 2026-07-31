from tkinter import DISABLED, END, NORMAL, RIGHT, LEFT, BOTH
from tkinter.ttk import Frame, Progressbar, Label
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

    self.progress_total = 0
    self.progress_current = 0

    progress_frame = Frame(self.FRAME)
    progress_frame.pack(fill='x', padx=10, pady=(10, 0))

    self.progress_bar = Progressbar(progress_frame, orient='horizontal', mode='determinate', maximum=1)
    self.progress_bar.pack(side='left', fill='x', expand=True)

    self.progress_label = Label(progress_frame, text="0/0 (0%)")
    self.progress_label.pack(side='left', padx=(10, 0))

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

  def reset_progress(self):
    """Reset the progress bar to an empty/unknown state, used before a new count is available"""
    self.progress_total = 0
    self.progress_current = 0
    self.progress_bar['maximum'] = 1
    self.progress_bar['value'] = 0
    self._update_progress_label()

  def set_progress_max(self, total: int):
    """Configure the progress bar with the total number of files to scan

    Args:
      total (int): total number of files that will be scanned
    """
    self.progress_total = max(total, 0)
    self.progress_current = 0
    self.progress_bar['maximum'] = max(total, 1)
    self.progress_bar['value'] = 0
    self._update_progress_label()

  def increment_progress(self, step: int = 1):
    """Advance the progress bar by step files scanned"""
    self.progress_current += step
    self.progress_bar['value'] = self.progress_current
    self._update_progress_label()
    self.progress_bar.update_idletasks()

  def _update_progress_label(self):
    percent = int((self.progress_current / self.progress_total) * 100) if self.progress_total else 0
    self.progress_label.config(text=f"{self.progress_current}/{self.progress_total} ({percent}%)")
