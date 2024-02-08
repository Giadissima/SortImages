from tkinter.ttk import Frame, Label
from src.ui.settings.settings_style import main_color, card_color
from src.files_manager.images import ImageHelper

class Card():
  def __init__(self, father_frame, title, side=None, padding=0, fill=None, expand=None, card_color='Card.TFrame') -> None:
    self.card_color = card_color
    self.title = title
    self.create_card(father_frame, side=side, padding=padding, fill=fill, expand=expand)
    self.configure_grid()
    
  def create_card(self, father_frame, side=None, padding=0, fill=None, expand=False):
    self.card_container = Frame(father_frame)
    self.card_container.pack(side=side, fill=fill, expand=expand) # fill in questo punto ha 20 a caso
    
    title_label = Label(self.card_container, text=self.title, background=main_color, foreground='white', padding=padding)
    title_label.grid(column=0, row=0, sticky='w')
    self.card = Frame(self.card_container, style=self.card_color)
    self.card.grid(column=0, row=1, sticky='ewsn')
  
  def configure_grid(self):
    self.card_container.grid_columnconfigure(0, weight=1)
    self.card_container.grid_rowconfigure(1, weight=1)
    
    
class ImageCard(Card):
  def __init__(self, father_frame, title, img, side=None, card_color='Card.TFrame', padding=0, fill=None, expand=None, img_width=230, img_height=350) -> None:
    self.img = ImageHelper.resize_image(img, img_width, img_height)
    # self.img = img
    super().__init__(father_frame, title, side=side, card_color=card_color, padding=padding, fill=fill, expand=expand)
    self.create_widgets()
    self.create_img()
    
  def create_widgets(self):
    self.widget_frame = Frame(self.card, style=self.card_color)
    self.widget_frame.pack(side='right')
    
  def create_img(self):
    # Crea un widget Canvas per visualizzare l'immagine
    # canvas = Canvas(self.card, width=self.img.width, height=self.img.height)
    img_container = Label(self.card, background=main_color, image=self.img)
    img_container.store_image = self.img
    img_container.pack(side='left')

    # Disegna l'immagine sul Canvas
    # canvas._image(0, 0, anchor="nw", image=self.img)
    
  