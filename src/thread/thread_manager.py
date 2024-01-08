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
    self.sort = Sort(self.quit_event, self.pause_event)
    
  def pause_sort(self, main_button: Button)->None:
    """pause the sort process

    Args:
      main_button (Button): The button inside the graphical interface whose text needs to be changed.
    """
    if self.sort_thread and self.sort_thread.is_alive():
      self.pause_event.set()
      main_button.config(text="Resume")

  def resume_sort(self, main_button: Button)->None:
    """resume the sort process

    Args:
      main_button (Button): The button inside the graphical interface whose text needs to be changed.
    """
    if self.sort_thread and self.sort_thread.is_alive():
      self.pause_event.clear()
      main_button.config(text="Pause")

  def start_sort(self, input_folder_entry:str, output_folder_entry:str, check_and_set_preference, main_button: Button):
    """start the sort process

    Args:
        input_folder_entry (str): the text entry containing the input folder path
        text_entry2 (str): the text entry containing the output folder path
        check_and_set_preference (function): Check the saved user preferences.'
        main_button (Button): The button inside the graphical interface whose text needs to be changed.
    """
    if self.sort_thread and self.sort_thread.is_alive():
      self.quit_event.set()  # Imposta l'evento di interruzione
      self.sort_thread.join()  # Attendi che il thread esistente termini completamente
      return
    self.sort_thread = None
    self.pause_event.clear()
    self.quit_event.clear()
    
    msg1 = "The program will delete duplicate images.\nIt will not be possible to recover them.\nContinue?"
    msg2 = "Are you sure you want to delete empty folders\nfrom the starting folder?"

    check_and_set_preference('DeleteDuplicates', msg1)
    check_and_set_preference('DeleteEmptyFolders', msg2)

    Config.set_input_folder(input_folder_entry)
    Config.set_output_folder(output_folder_entry)
    
    self.sort_thread = Thread(target=self.run_sort, args=(main_button,))
    self.sort_thread.start()
    main_button.config(text="Pause")
    
  def run_sort(self, main_button:Button):
    """Starts the thread that will organize the files.

    Args:
      main_button (Button): The button inside the graphical interface whose text needs to be changed.
    """
    while not self.quit_event.is_set():
      if not self.pause_event.is_set():
        result, msg = self.sort.start_sort()
        if result:
          messagebox.showinfo(title="Success", message="Sort completed")
        else:
          messagebox.showerror(title="Error", message=msg)
        try:
          main_button.config(text="Start")
        except RuntimeError:
          pass
        finally:
          self.quit_event.set()
          self.sort_thread = None
        break

    
  def on_close(self):
    """Closes the thread properly"""
    if self.sort_thread and self.sort_thread.is_alive():
      self.sort.quit()
      self.sort_thread.join(timeout=3)