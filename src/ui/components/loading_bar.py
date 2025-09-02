import tkinter as tk
from tkinter import ttk
import time

class LoadingBar():
  def __init__(self, root):
    self.start_progress()
    self.root = root
    self.progress = ttk.Progressbar(self.root, orient="horizontal",
                          length=300, mode="determinate")
    
  def start_progress(self):
    self.progress["value"] = 0
    self.root.update_idletasks()
    for i in range(101):
        self.progress["value"] = i
        self.root.update_idletasks()
        time.sleep(0.05)  # simulazione di lavoro