from tkinter.ttk import Frame, Label
from src.ui.settings.settings_style import main_color
from src.files_manager.images import ImageHelper
class Card():
  """This class mimics the concept of a card in the context of web development.
  It creates a differently colored frame compared to the background with a title and components inside."""
  def __init__(self, father_frame:Frame, title:str,
               side:str|None=None, padding:int=0,
               fill:str=None, expand:bool=None,
               card_color:str='Card.TFrame') -> None:
    """Args:
        father_frame (Frame): the frame where to insert the card
        title (str): the title to insert on the card
        side (str, optional): the side where to align the card. Defaults to None.
        padding (int, optional): padding inside the card. Defaults to 0.
        fill (str, optional): the axis where to fill the card. Defaults to None.
        expand (bool, optional): Set True to make the card occupy more space. Defaults to False.
        card_color (str, optional): the style of the card. Default to 'Card.TFrame'.
        """
  
    self.card_color = card_color
    self.title = title
    self.create_card(father_frame, side=side, padding=padding, fill=fill, expand=expand)
    self.configure_grid()
    
  def create_card(self, father_frame:Frame, side:str|None=None, padding:int=0, fill:str=None, expand:bool=None):
    """Create a new simple card

    Args:
      father_frame (Frame): the frame where to insert the card
      side (str, optional): the side where to align the card. Defaults to None.
      padding (int, optional): padding inside the card. Defaults to 0.
      fill (str, optional): the axis where to fill the card. Defaults to None.
      expand (bool, optional): Set True to make the card occupy more space. Defaults to False.
    """
    self.card_container = Frame(father_frame)
    self.card_container.pack(side=side, fill=fill, expand=expand)
    
    title_label = Label(self.card_container, text=self.title, background=main_color, foreground='white', padding=padding)
    title_label.grid(column=0, row=0, sticky='w')
    self.card = Frame(self.card_container, style=self.card_color)
    self.card.grid(column=0, row=1, sticky='ewsn')
  
  def configure_grid(self):
    self.card_container.grid_columnconfigure(0, weight=1)
    self.card_container.grid_rowconfigure(1, weight=1)
    
    
class ImageCard(Card):
  """It extends the card class by creating one with an image to the left relative to the rest of the components."""
  def __init__(self, father_frame:Frame, title:str,
               img_path:str, side:str=None, card_color:str='Card.TFrame',
               padding:int=0, fill:str=None, expand:bool=None,
               img_width:int=200, img_height:int=350) -> None:
    """Args:
        father_frame (Frame): the frame where to insert the card
        title (str): the title to insert on the card
        img_path (str): The path of the image to put on the card
        side (str, optional): the side where to align the card. Defaults to None.
        card_color (str, optional): the style of the card. Default to 'Card.TFrame'.
        padding (int, optional): padding inside the card. Defaults to 0.
        fill (str, optional): the axis where to fill the card. Defaults to None.
        expand (bool, optional): Set True to make the card occupy more space. Defaults to False.
        img_width (int, optional): The width of the image inside the card. Defaults to 200.
        img_height (int, optional): The height of the image inside the card. Defaults to 350.
    """
    self.img = ImageHelper.resize_image(img_path, img_width, img_height)
    # self.img = img
    super().__init__(father_frame, title, side=side, card_color=card_color, padding=padding, fill=fill, expand=expand)
    self.create_widgets()
    self.create_img()
    
  def create_widgets(self):
    self.widget_frame = Frame(self.card, style=self.card_color)
    self.widget_frame.pack(side='right')
    
  def create_img(self):
    img_container = Label(self.card, background=main_color, image=self.img)
    img_container.store_image = self.img
    img_container.pack(side='left')