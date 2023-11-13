from tkinter import W, Checkbutton, IntVar

def create_opt_frame(frame, font=None):
    options = [
      "Sposta file non identificati nella cartella \"Unknown\"",
      "Sposta file duplicati nella cartella \"Duplicates\"",
      "Cancella cartelle rimaste vuote",
      "Mantieni organizzazione parziale delle cartelle di input"
    ]

    choices = []
    
    for i in range(0, len(options)):
      choices.append(IntVar())
      Checkbutton(frame, text=options[i], variable=choices[-1], font=font).grid(row=i, sticky=W)