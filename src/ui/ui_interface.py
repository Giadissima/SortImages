from tkinter import BOTH, Frame, Tk, messagebox
from tkinter.ttk import Label, Button

from src.sort import start_sort


from src.ui.tkinter_logs import TkinterLogs
from src.ui.style import configure_style
from src.config import Config
from src.ui.custom_messagebox import CustomMessageBox
from src.ui.user_config import ConfigManager
from src.ui.ui_manager import UIManager

class Interface():
  def __init__(self, title: str, size: str, icon_path: str, default_font=None, default_font_size=None):
    self.root = Tk()
    self.config = Config()
    self.config_manager = ConfigManager()
    self.ui_manager = UIManager(self.root, size, title, icon_path, default_font, default_font_size)
    
    self.main_frame()

  def main_frame(self):
    self.ui_manager.setup_ui()

    # TODO come funziona lo scoping di style?
    configure_style()

    btn = Button(self.root, text="Start", style="B.TButton", command=self.start_sort)
    btn.pack(pady=10)

    self.config.set_logs_obj(TkinterLogs(self.root))
    self.root.mainloop()

  def start_sort(self):
    msg1 = "The program will delete duplicate images.\nIt will not be possible to recover them.\nContinue?"
    msg2 = "Are you sure you want to delete empty folders\nfrom the starting folder?"

    self.check_and_set_preference('DUPLICATES_CHOISE', msg1)
    self.check_and_set_preference('FOLDER_CHOICE', msg2)

    self.config.set_input_folder(self.path_entry[0].get())
    self.config.set_output_folder(self.path_entry[1].get())
    result, msg = start_sort()
    if result:
      messagebox.showinfo(title="Success", message="Sort completed")
    else:
      messagebox.showerror(title="error", message=msg)

  def check_and_set_preference(self, preference_name, msg):
    checkbox = Config.checkbox_choises[preference_name], 
    if checkbox.get() == 1 and not self.config_manager.has_preference(preference_name):
      custom_message_box = self.ask_to_custom_msgbox(
        msg, preference_name)
      if not custom_message_box:
        checkbox.set(0)

  def ask_to_custom_msgbox(self, message, choise_name, title='Warning'):
    custom_message_box = CustomMessageBox(
      self.root,
      title,
      message,
      icon=self.icon_path
    )
    self.root.wait_window(custom_message_box)

    # TODO ho aggiunto == 1, controllarlo
    if custom_message_box.checkbox_var.get() == 1:
      self.config_manager.set_preference(choise_name, 'True')
    return custom_message_box.ok
  
  
