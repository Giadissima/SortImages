from tkinter import W, Checkbutton, Frame, IntVar, Label

from src.config.config import Config

class OptionsFrame:
  def __init__(self, frame, font=None):
    self.parent_frame = frame
    self.frame = Frame(self.parent_frame)
    self.font = font
    self.choices = {}
    self.create_opt_frame()

  def create_opt_frame(self):
    sub_title = Label(self.frame, text="Options", font='Noto 10 bold')
    sub_title.grid(row=0, sticky='w')

    options = {
      "DeleteDuplicates": "Delete duplicate images and videos from start folder",
      "DeleteEmptyFolders": "Delete empty folders after the sort process",
      "IgnoreFolderSort": "Do not consider folder names for sorting",
    }

    # idx = l'indice per memorizzare a che riga della griglia sei, 
    # enumerate(options) = restituisce una tupla con chiave e testo del dizionario, memorizzate poi come variabili nelle parentesi
    for idx, (key, text) in enumerate(options.items(), start=1):
      self.choices[key] = IntVar()
      Checkbutton(self.frame, text=text, variable=self.choices[key], font=self.font).grid(row=idx, sticky=W)

    Config.set_checkbox_choises(self.choices)

# Usage example:
# options_frame = OptionsFrame(frame, font)
