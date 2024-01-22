from tkinter import Canvas
from tkinter.ttk import Frame, Label
from src.ui.settings.settings_style import main_color
from src.files_manager.images import ImageHelper

class Card():
  def __init__(self, father_frame, title, side=None, padding=None, fill=None, expand=None, card_color='Card.TFrame') -> None:
    self.title = title
    self.create_card(father_frame, card_color=card_color, side=side, padding=padding, fill=fill, expand=expand)
    self.configure_grid()
    
  def create_card(self, father_frame, card_color='Card.TFrame', side=None, padding=None, fill=None, expand=None):
    self.card_container = Frame(father_frame, padding=padding)
    self.card_container.pack(side=side, fill=fill, expand=expand)
    
    title_label = Label(self.card_container, text=self.title, background=main_color, foreground='white')
    title_label.grid(column=0, row=0, sticky='w')
    self.card = Frame(self.card_container, style=card_color)
    self.card.grid(column=0, row=1, sticky='ewsn')
  
  def configure_grid(self):
    self.card_container.grid_columnconfigure(0, weight=1)
    self.card_container.grid_rowconfigure(1, weight=1)
    
    
class ImageCard(Card):
  def __init__(self, father_frame, title, img, side=None, padding=None, fill=None, expand=None, img_width=200, img_height=300) -> None:
    self.img = ImageHelper.resize_image(img, img_width, img_height)
    # self.img = img
    super().__init__(father_frame, title, side, padding, fill, expand)
    self.create_widgets()
    self.create_img()
    
  def create_widgets(self):
    self.widget_frame = Frame(self.card, style='Card.TFrame')
    self.widget_frame.pack(side='right')
    
  def create_img(self):
    # Crea un widget Canvas per visualizzare l'immagine
    # canvas = Canvas(self.card, width=self.img.width, height=self.img.height)
    img_container = Label(self.card, background=main_color, image=self.img)
    img_container.store_image = self.img
    img_container.pack(side='left')

    # Disegna l'immagine sul Canvas
    # canvas._image(0, 0, anchor="nw", image=self.img)
    
  