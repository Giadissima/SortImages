from tkinter import BOTH
from tkinter.ttk import Frame, Label
from src.ui.components.options_interface import OptionsFrame
from src.ui.components.tkinter_logs import TkinterLogs
from src.ui.components.folder_selection import FolderSelection
from src.ui.components.cards import create_card
from src.ui.utility.utility import configure_weight
from src.ui.settings.settings_style import main_color
from src.config.config import Config
from src.files_manager.images import ImageHelper

class UIManager:
  def __init__(self, root: Frame, size, title, icon_path):
    self.root: Frame = root
    self.size = size
    self.title = title
    self.icon_path = icon_path

  def setup_ui(self):
    title = self.setup_title()
    title.pack(side='top', pady=(20,20))

    form_frame = Frame(self.root)
    form_frame.pack(expand=True, fill=BOTH)

    self.setup_main_frame()
    self.setup_selection_folder_frame(form_frame)
    self.setup_options_frame(form_frame)
    self.setup_logs_widget()

    configure_weight(form_frame, [0], [0,1])

  def setup_selection_folder_frame(self, parent_frame):
    self.folder_selection_frame = FolderSelection(parent_frame, self.icon_path)
    self.folder_selection_frame.frame.grid(row=0, column=0, padx=10, sticky="nsew")
    
  def setup_options_frame(self, parent_frame):
    opt_frame = OptionsFrame(parent_frame)
    opt_frame.frame.grid(row=0, column=1, sticky="nsew")
    
  def setup_title(self):
    title_img = ImageHelper.resize_image('assets/title.png', 344, 69)
    title = Label(self.root, background=main_color, image=title_img)
    title.image= title_img
    return title
  
  def setup_logs_widget(self):
    log_frame = create_card(self.root, "Logs", side='bottom')
    Config.set_logs_obj(TkinterLogs(log_frame))

  def get_text_entries(self):
    input_folder = self.folder_selection_frame.folder_path_entries["input_folder"].get()
    output_folder = self.folder_selection_frame.folder_path_entries["output_folder"].get()
    return input_folder, output_folder
  
  def setup_main_frame(self):
    self.root.title(self.title)
    self.root.geometry(self.size)
    self.root.iconbitmap(self.icon_path)
    self.root.configure(bg=main_color)
