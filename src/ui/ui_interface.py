from tkinter import Tk
from tkinter.ttk import Button

from src.config.config import Config
from src.config.user_config import ConfigManager
from src.ui.components.tkinter_logs import TkinterLogs
from src.ui.settings.settings_style import configure_style
from src.ui.components.custom_messagebox import CustomMessageBox
from src.ui.ui_manager import UIManager
from src.thread_manager import ThreadManager

class Interface():
  def __init__(self, title: str, size: str, icon_path: str, default_font=None, default_font_size=None):
    self.root = Tk()
    self.config_manager = ConfigManager()
    self.icon_path = icon_path
    self.ui_manager = UIManager(self.root, size, title, icon_path, default_font, default_font_size)
    self.thread_manager = ThreadManager()
    self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    self.main_frame()

  def main_frame(self):
    self.ui_manager.setup_ui()

    # TODO come funziona lo scoping di style?
    configure_style()

    self.btn = Button(self.root, text="Start", style="B.TButton", command=self.thread_manager.start_sorting_or_resume)
    self.btn.pack(pady=10)

    Config.set_logs_obj(TkinterLogs(self.root))
    self.root.mainloop()

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
    self.thread_manager.on_close()
    self.root.destroy()