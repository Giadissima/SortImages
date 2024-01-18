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
    form_frame.pack(expand=True, fill=BOTH, padx=50)

    self.setup_main_frame()
    self.setup_selection_folder_frame(form_frame)
    self.setup_options_frame(form_frame)
    self.setup_logs_widget(self.root)

    configure_weight(form_frame, [0], [0,1])

  def setup_selection_folder_frame(self, parent_frame):
    folder_container_frame = create_card(parent_frame, "Folders selection", side='left')
    folder_container_frame.configure()
    self.folder_selection_frame = FolderSelection(folder_container_frame, self.icon_path)
    self.folder_selection_frame.frame.grid(row=0, column=0, padx=10, sticky="nsew")
    
  def setup_options_frame(self, parent_frame):
    opt_container_frame = create_card(parent_frame, "Options", side='right')
    opt_frame = OptionsFrame(opt_container_frame)
    opt_frame.frame.grid(row=0, column=1, sticky="nsew")
    
  def setup_title(self):
    title_img = ImageHelper.resize_image('assets/title.png', 344, 69)
    title = Label(self.root, background=main_color, image=title_img)
    title.image= title_img
    return title
  
  def setup_logs_widget(self, parent_frame):
    log_frame = create_card(parent_frame, "Logs", side='bottom')
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
