from threading import Event, Thread
from tkinter import Frame, messagebox
from src.sort.sort import start_sort
from src.config.config import Config

class ThreadManager():
  def __init__(self) -> None:
    self.pause_event = Event()  # Oggetto Event per gestire la pausa
    self.quit_event = Event()  # Oggetto Event per gestire la pausa
    self.sort_thread = None
    
  def start_sorting_or_resume(self):
    # Verifica se il thread di ordinamento è già in esecuzione
    if self.sort_thread: # se il thread esiste
      if self.sort_thread.is_alive(): # se è vivo
        if self.pause_event and self.pause_event.is_set(): # dobbiamo fare il resume
          print('resuming....')
          self.resume_sort()
        else: # dobbiamo fare il pause
          # Il thread è in esecuzione, lo vogliamo mettere in pausa
          print('pausing....')
          self.pause_sort()
    else:
      print('starting....')
      self.start_sort()

  def pause_sort(self):
    if self.sort_thread and self.sort_thread.is_alive():
      self.pause_event.set()
      self.btn.config(text="Resume")

  def resume_sort(self):
    if self.sort_thread and self.sort_thread.is_alive():
      self.pause_event.clear()
      self.btn.config(text="Pause")

  def start_sort(self):
    self.pause_event.clear()
    self.quit_event.clear()
    self.btn.config(text="Pause")
    
    msg1 = "The program will delete duplicate images.\nIt will not be possible to recover them.\nContinue?"
    msg2 = "Are you sure you want to delete empty folders\nfrom the starting folder?"

    self.check_and_set_preference('DeleteDuplicates', msg1)
    self.check_and_set_preference('DeleteEmptyFolders', msg2)

    Config.set_input_folder(self.ui_manager.path_entry[0].get())
    Config.set_output_folder(self.ui_manager.path_entry[1].get())
    
    self.sort_thread = Thread(target=self.run_sort)
    self.sort_thread.start()
    
  def run_sort(self):
    result, msg = start_sort(pause_event=self.pause_event, quit_event=self.quit_event)
    if result:
      messagebox.showinfo(title="Success", message="Sort completed")
    else:
      messagebox.showerror(title="Error", message=msg)
    self.btn.config(text="Start")
    self.quit_event.set()
    
  def on_close(self):
    if self.sort_thread and self.sort_thread.is_alive():
      self.quit_event.set()
      self.sort_thread.join(timeout=3)