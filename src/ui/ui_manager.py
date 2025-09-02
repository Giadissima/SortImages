from tkinter import BOTH, Image, PhotoImage
from tkinter.ttk import Frame, Label
from assets.load_img import CAT_IMG_PATH, FOLDER_CARD_IMG_PATH, FOLDER_IMG_PATH, LINUX_ICON, MAC_ICON, WINDOWS_ICON, TITLE_IMG_PATH
from src.ui.components.options_interface import OptionsFrame
from src.ui.components.tkinter_logs import TkinterLogs
from src.ui.components.folder_selection import FolderSelection
from src.ui.components.cards import Card, ImageCard
from src.ui.utility.utility import configure_weight
from src.ui.settings.settings_style import main_color
from src.config.config import Config
from src.files_manager.images import ImageHelper

class UIManager:
  def __init__(self, root: Frame, size:str, title:str):
    """
    This class is responsible for initializing all the graphical components inside the main frame.

    Args:
      root (Frame): the main frame
      size (str): a string of main frame's size with '<width>x<height>' format (es. 500x600)
      title (str): The title of the main frame
    """
    self.root: Frame = root
    self.size = size
    self.title = title

  def setup_ui(self):
    self.setup_title()

    form_frame = Frame(self.root)
    form_frame.pack(expand=True, fill=BOTH, padx=50)

    self.setup_main_frame()
    self.setup_selection_folder_frame(form_frame)
    self.setup_options_frame(form_frame)
    self.setup_logs_widget(self.root)

    configure_weight(form_frame, [0], [0,1])

  def setup_selection_folder_frame(self, parent_frame:Frame):
    self.folder_container_frame = Frame(parent_frame)
    # self.folder_container_frame = Frame(parent_frame, style=self.card_color) # TODO
    self.folder_container_frame.pack()
    self.folder_selection_frame = FolderSelection(self.folder_container_frame, FOLDER_IMG_PATH).frame.pack()
    
  def setup_options_frame(self, parent_frame):
    """generate a card with an image containing the various sorting options"""
    opt_container_frame = Frame(parent_frame).pack()
    opt_frame = OptionsFrame(opt_container_frame)
    opt_frame.frame.pack()
    
  def setup_title(self):
    """generate a Label containing title's img"""
    title_img = ImageHelper.resize_image(TITLE_IMG_PATH, 344, 69)
    title = Label(self.root, background=main_color, image=title_img, padding=0)
    title.image= title_img
    title.pack(side='top', pady=(10,0))
  
  def setup_logs_widget(self, parent_frame):
    """Create a card containing a read-only textarea that will serve as the program logger."""
    log_card = Card(parent_frame, "Logs", side='bottom', expand=False, fill='x', card_color='TFrame', padding=(10,0))
    Config.set_logs_obj(TkinterLogs(log_card.card))

  def get_folders_path(self):
    """get folders' path strings previously selected in the ui interface"""
    input_folder = self.folder_selection_frame.folder_path_entries["input_folder"].get()
    output_folder = self.folder_selection_frame.folder_path_entries["output_folder"].get()
    return input_folder, output_folder
  
  def setup_main_frame(self):
    """setup general options of the main frame"""
    self.root.title(self.title)
    self.root.geometry(self.size)
    if Config.os_system == 'Windows': self.root.iconbitmap(WINDOWS_ICON)
    elif Config.os_system == 'Linux': 
      img = Image("photo", file=LINUX_ICON)
      self.root.iconphoto(False, img)
    else:
      # img = Image("photo", file=MAC_ICON) # TODO bug
      # self.root.iconphoto(False, img)
      pass
    self.root.configure(bg=main_color)
    self.root.configure(bg=main_color)
