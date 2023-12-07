import sys
from threading import Thread, Event
import time
from tkinter import Tk, messagebox
from tkinter.ttk import Button

from src.config.config import Config
from src.config.user_config import ConfigManager
from src.sort.sort import start_sort
from src.ui.components.tkinter_logs import TkinterLogs
from src.ui.settings.settings_style import configure_style
from src.ui.components.custom_messagebox import CustomMessageBox
from src.ui.ui_manager import UIManager

class Interface():
  def __init__(self, title: str, size: str, icon_path: str, default_font=None, default_font_size=None):
    self.root = Tk()
    self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    self.config_manager = ConfigManager()
    self.icon_path = icon_path
    self.ui_manager = UIManager(self.root, size, title, icon_path, default_font, default_font_size)
    self.sort_thread = None  # Variabile per tenere traccia del thread di ordinamento
    self.pause_event = Event()  # Oggetto Event per gestire la pausa
    self.quit_event = Event()  # Oggetto Event per gestire la pausa
    
    self.main_frame()

  def main_frame(self):
    self.ui_manager.setup_ui()

    # TODO come funziona lo scoping di style?
    configure_style()

    self.btn = Button(self.root, text="Start", style="B.TButton", command=self.start_sorting_or_resume)
    self.btn.pack(pady=10)

    Config.set_logs_obj(TkinterLogs(self.root))
    self.root.mainloop()

  # TODO metterlo in un file thread?
  def start_sorting_or_resume(self):
    # Verifica se il thread di ordinamento è già in esecuzione
    if self.sort_thread: # se il thread esiste
      if self.sort_thread.is_alive(): # se è vivo
        if self.pause_event and self.pause_event.is_set(): # dobbiamo fare il resume
          print('resuming....')
          self.resume_sort()
        else: # dobbiamo fare il pause
          # Il thread è in esecuzione, quindi vuoi metterlo in pausa
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

  def check_and_set_preference(self, preference_name, msg):
    if Config.get_checkbox_choises(preference_name) and not self.config_manager.has_preference(preference_name):
      self.ask_to_custom_msgbox(msg, preference_name)

  def ask_to_custom_msgbox(self, message, choise_name, title='Warning'):
    custom_message_box = CustomMessageBox(
      self.root,
      title,
      message,
      icon=self.icon_path
    )
    self.root.wait_window(custom_message_box)

    # TODO ho aggiunto == 1, controllarlo
    checkbox = custom_message_box.checkbox_var
    if checkbox.get() == 1:
      self.config_manager.set_preference(choise_name, 'True')
    return custom_message_box.ok
  
  def on_close(self):
    print("ciao")
    if self.sort_thread and self.sort_thread.is_alive():
      self.quit_event.set()
      print("setting")
      self.sort_thread.join(timeout=3)
      # self.sort_thread = None # TODO non lo cancella dalla memoria! trovare un modo per killarlo

      # Chiudi la finestra Tkinter
    self.root.destroy()
