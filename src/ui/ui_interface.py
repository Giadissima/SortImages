from tkinter import Tk
from assets.load_img import ROUNDED_BUTTON_IMG_PATH

from src.config.config import Config
from src.config.user_config import ConfigManager

from src.ui.settings.settings_style import configure_style
from src.ui.components.custom_messagebox import CustomMessageBox
from src.ui.ui_manager import UIManager
from src.thread.thread_manager import ThreadManager
from src.ui.components.buttons import create_rounded_button

class Interface():
  """
  This class generates the program window and communicates
  with UiManager to initialize internal components as well.
  """
  def __init__(self, title: str, size: str):
    self.root = Tk()
    configure_style() 
    self.config_manager = ConfigManager()
    self.ui_manager = UIManager(self.root, size, title)
    self.thread_manager = ThreadManager()
    self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    self.main_frame()

  def main_frame(self):
    self.ui_manager.setup_ui()
    self.btn = create_rounded_button(self.root, ROUNDED_BUTTON_IMG_PATH, 100, 40, command=self.start_thread)
    self.btn.pack(side='bottom')

    try:
      self.root.mainloop()
    except KeyboardInterrupt:
      print("chiusura...")
    
  def ask_to_custom_msgbox(self, message, choise_name, title='Warning'):
    custom_message_box = CustomMessageBox(
      self.root,
      title,
      message,
    )
    self.root.wait_window(custom_message_box)

    checkbox = custom_message_box.checkbox_var
    if checkbox.get() == 1:
      self.config_manager.set_preference(choise_name, 'True')
    return custom_message_box.ok_button

  def on_close(self):
    self.thread_manager.kill_thread()
    self.root.destroy()
    
  def check_and_set_preference(self, preference_name, msg):
    if Config.get_checkbox_choises(preference_name) and not self.config_manager.has_preference(preference_name):
      return self.ask_to_custom_msgbox(msg, preference_name)
      
  def start_thread(self):
    """ Check if the button to start or pause the sorting process has been pressed. """
    # Check if the sorting thread is already running
    input_folder, output_folder = self.ui_manager.get_folders_path()
    self.thread_manager.start_thread(input_folder, output_folder, self.check_and_set_preference, self.btn)