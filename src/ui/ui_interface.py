from tkinter import Tk
from tkinter.ttk import Button

from src.config.config import Config
from src.config.user_config import ConfigManager
from src.ui.components.tkinter_logs import TkinterLogs
from src.ui.settings.settings_style import configure_style
from src.ui.components.custom_messagebox import CustomMessageBox
from src.ui.ui_manager import UIManager
from src.thread.thread_manager import ThreadManager

class Interface():
  def __init__(self, title: str, size: str, icon_path: str):
    self.icon_path = icon_path
    self.root = Tk()
    self.config_manager = ConfigManager()
    self.ui_manager = UIManager(self.root, size, title, icon_path)
    self.thread_manager = ThreadManager()
    
    self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    self.main_frame()

  def main_frame(self):
    self.ui_manager.setup_ui()
    configure_style()
    self.btn = Button(
      self.root, 
      text="Start", 
      style="StartButton.TButton",
      command=self.start_sorting_or_resume)
    self.btn.pack(pady=10)

    Config.set_logs_obj(TkinterLogs(self.root))
    try:
      self.root.mainloop()
    except KeyboardInterrupt:
      print("chiusura...")
    
  def ask_to_custom_msgbox(self, message, choise_name, title='Warning'):
    custom_message_box = CustomMessageBox(
      self.root,
      title,
      message,
      icon=self.icon_path
    )
    self.root.wait_window(custom_message_box)

    checkbox = custom_message_box.checkbox_var
    if checkbox.get() == 1:
      self.config_manager.set_preference(choise_name, 'True')
    return custom_message_box.ok_button

  def on_close(self):
    self.thread_manager.on_close()
    self.root.destroy()
    
  def check_and_set_preference(self, preference_name, msg):
    if Config.get_checkbox_choises(preference_name) and not self.config_manager.has_preference(preference_name):
      self.ask_to_custom_msgbox(msg, preference_name)
      
  def start_sorting_or_resume(self):
    """ Check if the button to start or pause the sorting process has been pressed. """
    # Check if the sorting thread is already running
    if self.thread_manager.sort_thread: # if thread exists
      if self.thread_manager.sort_thread.is_alive(): # if it's alive
        if self.thread_manager.pause_event and self.thread_manager.pause_event.is_set(): # we need to perform the resume action
          print('resuming....')
          self.thread_manager.resume_sort(self.btn)
        else: # dobbiamo fare il pause
          # Il thread è in esecuzione, lo vogliamo mettere in pausa
          print('pausing....')
          self.thread_manager.pause_sort(self.btn)
    else:
      print('starting....')
      input_folder, output_folder = self.ui_manager.get_text_entries()
      self.thread_manager.start_sort(input_folder, output_folder, self.check_and_set_preference, self.btn)