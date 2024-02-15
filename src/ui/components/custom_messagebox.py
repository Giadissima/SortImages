from tkinter.ttk import Frame, Label, Checkbutton
from tkinter import BooleanVar, LEFT, RIGHT, Toplevel
from assets.load_img import OK_BUTTON_PATH, UNDO_BUTTON_PATH, WARNING_IMG_PATH
from src.files_manager.images import ImageHelper
from src.ui.settings.settings_style import main_color
from src.ui.components.buttons import create_rounded_button

class CustomMessageBox(Toplevel):
  """
  This class generates a custom messagebox that asks the user if they are
  sure about a certain decision passed as a parameter. The user will have
  the option to respond by choosing to proceed or cancel through two buttons.
  """
  def __init__(self, parent: Frame, title:str, message:str, icon=None)->None:
    super().__init__(parent)
    self.title(title)
    self.ok_button = False
    self.message = message
    self.config(bg=main_color)

    if icon:
      self.iconbitmap(default=icon)

    self.geometry("550x400")
    self.create_widgets()
      
  def create_widgets(self)->None:
    """Creates buttons and labels necessary to interface"""
    self.warning_img_path = ImageHelper.resize_image(WARNING_IMG_PATH, 120, 100)
    label = Label(self, text="Warning", style='MsgBoxTitle.TLabel')
    
    label1 = Label(self, image=self.warning_img_path, background=main_color, padding=15)
    label1.image = self.warning_img_path
    label.pack()
    label1.pack()

    self.message_label = Label(self, text=self.message, padding=10, style="MsgBoxSubtitle.TLabel")
    self.message_label.pack()

    self.checkbox_var = BooleanVar()
    self.dont_show_again_checkbox = Checkbutton(self, text="Don't show again", variable=self.checkbox_var, style='MsgBoxTitle.TCheckbutton')
    self.dont_show_again_checkbox.pack()

    button1 = create_rounded_button(self, UNDO_BUTTON_PATH, 135, 50, command=lambda: self.button_pressed(False))
    button2 = create_rounded_button(self, OK_BUTTON_PATH, 135, 50, command=lambda: self.button_pressed(True))

    button1.pack(side=LEFT, padx=35, ipadx=10)
    button2.pack(side=RIGHT, padx=35, ipadx=10)

  def button_pressed(self, is_ok:bool):
    """Quit the custom messagebox
    
    Args:
      is_ok(bool): checks if button pressed is the ok button"""
    self.ok_button = is_ok
    self.destroy()
