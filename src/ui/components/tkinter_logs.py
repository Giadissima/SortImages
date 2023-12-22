from tkinter import BOTH, DISABLED, END, NORMAL, Frame
from tkinter.scrolledtext import ScrolledText

class TkinterLogs():
  def __init__(self, frame:Frame):
    """Configure initial tags and the logs widget
    Args:
      frame (Frame): root frame where to pack the logs widget"""
    self.FRAME = frame
    self.log_text_field = ScrolledText(self.FRAME, height=10, width=30, state=DISABLED)
    self.log_text_field.tag_configure('error', foreground='red')
    self.log_text_field.tag_configure('info', foreground='blue')
    self.log_text_field.tag_configure('debug', foreground='black')
    self.log_text_field.pack(expand=True, fill=BOTH, padx=10, pady=10)
    
  def add_logs(self, message:str, tag:str):
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