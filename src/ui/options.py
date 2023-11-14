from tkinter import W, Checkbutton, IntVar, Label

from src.config import Config

def create_opt_frame(frame, font=None):
  config = Config()
  sub_title = Label(frame, text="Options", font='Noto 10 bold')
  sub_title.grid(row=0, sticky='w')
  options = [
    "Delete duplicate images and videos from start folder",
    "Delete empty folders after the sort process",
  ]

  choices = []
  
  for i in range(0, len(options)):
    choices.append(IntVar())
    Checkbutton(frame, text=options[i], variable=choices[-1], font=font).grid(row=i+1, sticky=W)
  
  config.set_checkbox_choises(choices)
  