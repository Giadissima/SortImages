from tkinter.ttk import Frame, Label
from src.ui.settings.settings_style import main_color

def create_card(father_frame, title, side=None):
  card_container_frame = Frame(father_frame, style='Prova.TFrame')
  title_label = Label(card_container_frame, text=title, background=main_color, foreground='white')
  card_frame = Frame(card_container_frame)
  title_label.grid(column=0, row=0, sticky='w', padx=10)
  card_frame.grid(column=0, row=1, sticky='ewsn')
  card_container_frame.pack(side=side, fill='both', expand=True)  # Cambiato fill da 'x' a 'both'
  card_container_frame.grid_columnconfigure(0, weight=1)
  card_container_frame.grid_rowconfigure(1, weight=1)  # Aggiunto per consentire l'espansione verticale
  return card_frame