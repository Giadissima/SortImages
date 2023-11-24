from tkinter import BOTH, Frame, Tk, messagebox
from tkinter.ttk import Label, Button, Style

from src.sort import start_sort
from src.ui.option import create_opt_frame
from src.ui.folder_selection import create_selection_folder_frame
from src.ui.log import Logs
from src.config import Config
from src.ui.custom_messagebox import CustomMessageBox
from configparser import ConfigParser
# TODO trasformare il tutto in una funzione con array associativi per le preferenze
# TODO usare i set per l'hashlist


class Interface():
  def __init__(self, title: str, size: str, icon_path: str, default_font=None, default_font_size=None):
    self.TITLE = title
    self.SIZE = size
    self.icon_path = icon_path
    self.default_font = default_font
    self.default_font_size = default_font_size
    self.root = Tk()
    self.config = Config()
    self.config_parser = ConfigParser()

    self.main_frame()

  def main_frame(self):
    self.read_config()

    self.root.title(self.TITLE)
    self.root.geometry(self.SIZE)
    self.root.iconbitmap(self.icon_path)

    self.style = Style()
    Style().configure("TButton", padding=3, background="white")
    self.style.map("B.TButton",
                    foreground=[('pressed', 'orange'),
                                ('active', 'orange'), ('!pressed', 'red')],
                    background=[
                        ('pressed', '!disabled', 'active', 'white')],
                    font='Noto 10 bold')

    title = Label(self.root, text=self.TITLE,
                  font='Noto 16 bold', padding=10)
    title.pack()

    form_frame = Frame(self.root)
    form_frame.pack(expand=True, fill=BOTH)

    selection_folder_frame = Frame(form_frame)
    selection_folder_frame.grid(row=0, column=0, padx=10, sticky="nsew")
    self.path_entry = create_selection_folder_frame(
        selection_folder_frame, self.icon_path, self.default_font)

    option_frame = Frame(form_frame)
    create_opt_frame(option_frame, self.default_font)
    option_frame.grid(row=0, column=1, sticky="nsew", padx=10)

    form_frame.columnconfigure(0, weight=1)
    form_frame.columnconfigure(1, weight=1)
    form_frame.rowconfigure(0, weight=1)

    btn = Button(self.root, text="Start",
                  style="B.TButton", command=self.start_sort)
    btn.pack(pady=10)

    self.config.set_logs_obj(Logs(self.root))
    self.root.mainloop()

  def read_config(self):
    self.config_parser.read('config.ini')
    if not self.config_parser.has_section('Preferences'):
      self.config_parser.add_section('Preferences')

  def start_sort(self):
    msg1 = "The program will delete duplicate images.\nIt will not be possible to recover them.\nContinue?"
    msg2 = "Are you sure you want to delete empty folders\nfrom the starting folder?"

    self.check_and_set_preference(Config.checkbox_choises[0], 'DUPLICATES_CHOISE', msg1)
    self.check_and_set_preference(Config.checkbox_choises[1], 'FOLDER_CHOICE', msg2)

    self.config.set_input_folder(self.path_entry[0].get())
    self.config.set_output_folder(self.path_entry[1].get())
    result, msg = start_sort()
    if result:
      messagebox.showinfo(title="Success", message="Sort completed")
    else:
      messagebox.showerror(title="error", message=msg)

  def check_and_set_preference(self, checkbox, preference_name, msg):
    if checkbox.get() == 1 and not self.config_parser.has_option('Preferences', preference_name):
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

    if custom_message_box.checkbox_var.get():
      with open('config.ini', "w") as configfile:
        self.config_parser.set('Preferences', choise_name, 'True')
        self.config_parser.write(configfile)

    return custom_message_box.ok
