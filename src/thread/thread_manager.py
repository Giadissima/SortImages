from threading import Event, Thread
from tkinter.ttk import Button
from tkinter import messagebox
from src.sort.sort import Sort
from src.config.config import Config

class ThreadManager():
  def __init__(self) -> None:
    self.pause_event = Event()  # Oggetto Event per gestire la pausa
    self.quit_event = Event()  # Oggetto Event per gestire la chiusura del processo
    self.sort_thread = None
    
  def pause_sort(self, main_button: Button):
    if self.sort_thread and self.sort_thread.is_alive():
      self.pause_event.set()
      main_button.config(text="Resume")

  def resume_sort(self, main_button: Button):
    if self.sort_thread and self.sort_thread.is_alive():
      self.pause_event.clear()
      main_button.config(text="Pause")

  def start_sort(self, text_entry1:str, text_entry2:str, check_and_set_preference, main_button: Button):
    if self.sort_thread != None and self.sort_thread.is_alive(): 
      print("sort_thread is not terminated")
      return
    self.sort_thread = None
    self.pause_event.clear()
    self.quit_event.clear()
    
    msg1 = "The program will delete duplicate images.\nIt will not be possible to recover them.\nContinue?"
    msg2 = "Are you sure you want to delete empty folders\nfrom the starting folder?"

    check_and_set_preference('DeleteDuplicates', msg1)
    check_and_set_preference('DeleteEmptyFolders', msg2)

    Config.set_input_folder(text_entry1)
    Config.set_output_folder(text_entry2)
    
    self.sort_thread = Thread(target=self.run_sort, args=(main_button,))
    self.sort_thread.start()
    main_button.config(text="Pause")
    
  def run_sort(self, main_button):
    self.sort = Sort(self.quit_event, self.pause_event)
    result, msg = self.sort.start_sort()
    if result:
      messagebox.showinfo(title="Success", message="Sort completed")
    else:
      messagebox.showerror(title="Error", message=msg)
    main_button.config(text="Start")
    self.quit_event.set()
    self.sort_thread = None
    
  def on_close(self):
    if self.sort_thread and self.sort_thread.is_alive():
      self.quit_event.set()
      self.sort_thread.join(timeout=3)