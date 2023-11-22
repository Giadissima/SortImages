from tkinter import Label, BooleanVar, Button, Checkbutton, LEFT, RIGHT, Toplevel
from src.ui.utils import resize_image
class CustomMessageBox(Toplevel):
  # TODO mettere style in configuration
  # TODO rivedere l'intera grafica e aggiungere il pulsante di warning
  def __init__(self, parent, title, message, icon=None):
    super().__init__(parent)
    self.title(title)
    self.ok = True

    if icon:
      self.iconbitmap(default=icon)

    self.geometry("350x180")

    self.warning_img_path = resize_image('assets/Warning.png', 70, 50)
    label1 = Label(self,image=self.warning_img_path)
    label1.image = self.warning_img_path  # Mantieni un riferimento
    label1.pack()
    
    self.message_label = Label(self, text=message, padx=10, pady=10)
    self.message_label.pack()

    self.checkbox_var = BooleanVar()
    self.checkbox = Checkbutton(self, text="Don't show again", variable=self.checkbox_var)
    self.checkbox.pack()

    self.ok_button = Button(self, text="OK", command=self.ok_pressed, highlightthickness=0)
    self.ok_button.pack(side=LEFT, padx=35, ipadx=10)

    self.cancel_button = Button(self, text="Cancel", command=self.cancel_pressed, highlightbackground='white')
    self.cancel_button.pack(side=RIGHT, padx=35, ipadx=10)
    

  def ok_pressed(self):
    self.ok = True
    self.destroy()

  def cancel_pressed(self):
    self.ok = False
    self.destroy()