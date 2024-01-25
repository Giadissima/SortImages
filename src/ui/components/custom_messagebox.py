from tkinter.ttk import Frame, Label, Button, Checkbutton
from tkinter import BooleanVar, LEFT, RIGHT, Toplevel
from assets.load_img import WARNING_IMG_PATH
from src.files_manager.images import ImageHelper

class CustomMessageBox(Toplevel):
  def __init__(self, parent: Frame, title:str, message:str, icon=None):
    self.buttons = {
      "OK": {"text": "OK", "command": lambda self: self.button_pressed(True)},
      "Cancel": {"text": "Cancel", "command": lambda self: self.button_pressed(False)}
    }
    super().__init__(parent)
    self.title(title)
    self.ok_button = True
    self.message = message

    if icon:
      self.iconbitmap(default=icon)

    self.geometry("350x180")

    self.create_widgets()
      
  def create_widgets(self):
    """ Creates buttons and labels necessary to interface"""
    self.warning_img_path = ImageHelper.resize_image(WARNING_IMG_PATH, 70, 50)
    label1 = Label(self, image=self.warning_img_path)
    label1.image = self.warning_img_path
    label1.pack()

    self.message_label = Label(self, text=self.message, padding=10)
    self.message_label.pack()

    self.checkbox_var = BooleanVar()
    self.dont_show_again_checkbox = Checkbutton(self, text="Don't show again", variable=self.checkbox_var)
    self.dont_show_again_checkbox.pack()

    for button_name, button_info in self.buttons.items():
      button = Button(self, text=button_info["text"], command=lambda: button_info["command"](self))

      button.pack(side=LEFT if button_name == "OK" else RIGHT, padx=35, ipadx=10)

  def button_pressed(self, is_ok:bool):
    """Quit the custom messagebox
    
    Args:
      is_ok(bool): checks if button pressed is the ok button"""
    self.ok_button = is_ok
    self.destroy()
