from tkinter import BOTH
from tkinter.ttk import Frame, Label
from assets.load_img import CAT_IMG_PATH, FOLDER_IMG_PATH, LOGO_IMG_PATH, TITLE_IMG_PATH
from src.ui.components.options_interface import OptionsFrame
from src.ui.components.tkinter_logs import TkinterLogs
from src.ui.components.folder_selection import FolderSelection
from src.ui.components.cards import Card, ImageCard
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
    title.pack(side='top', pady=(10,0))

    form_frame = Frame(self.root)
    form_frame.pack(expand=True, fill=BOTH, padx=50)

    self.setup_main_frame()
    self.setup_selection_folder_frame(form_frame)
    self.setup_options_frame(form_frame)
    self.setup_logs_widget(self.root)

    configure_weight(form_frame, [0], [0,1])

  def setup_selection_folder_frame(self, parent_frame):
    folder_container_frame = ImageCard(parent_frame, "Folders selection", "assets/prova3.jpeg", side='left', img_width=235)
    self.folder_selection_frame = FolderSelection(folder_container_frame.widget_frame, FOLDER_IMG_PATH)
    self.folder_selection_frame.frame.grid(row=0, column=0, padx=10, sticky="nsew", pady=31)
    
  def setup_options_frame(self, parent_frame):
    opt_container_frame = ImageCard(parent_frame, "Options", CAT_IMG_PATH, side='right', img_width=235)
    opt_frame = OptionsFrame(opt_container_frame.widget_frame)
    opt_frame.frame.grid(row=0, column=1, sticky="new", padx=10, pady=10)
    
  def setup_title(self):
    title_img = ImageHelper.resize_image(TITLE_IMG_PATH, 344, 69)
    title = Label(self.root, background=main_color, image=title_img, padding=0)
    title.image= title_img
    return title
  
  def setup_logs_widget(self, parent_frame):
    log_card = Card(parent_frame, "Logs", side='bottom', expand=False, fill='x', card_color='TFrame', padding=(10,0))
    Config.set_logs_obj(TkinterLogs(log_card.card))

  def get_text_entries(self):
    input_folder = self.folder_selection_frame.folder_path_entries["input_folder"].get()
    output_folder = self.folder_selection_frame.folder_path_entries["output_folder"].get()
    return input_folder, output_folder
  
  def setup_main_frame(self):
    self.root.title(self.title)
    self.root.geometry(self.size)
    self.root.iconbitmap(self.icon_path)
    self.root.configure(bg=main_color)
