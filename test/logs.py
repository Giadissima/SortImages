from tkinter import DISABLED, END, NORMAL, Button, Entry, Text

class Logs():
  def __init__(self, frame) -> None:
    self.FRAME = frame
    self.create_logs_frame()
    
  def add_logs(self, message):
      self.log_text_field.config(state=NORMAL)  # Abilita la modifica del testo
      self.log_text_field.insert(END, f"{message}\n")
      self.log_text_field.config(state=DISABLED)  # Disabilita la modifica del testo
      
  def create_logs_frame(self):
    # Finestra di log
    log_text_field = Text(self.FRAME, height=10, width=30, state=DISABLED)
    log_text_field.pack()

    # Input field
    input_entry = Entry(self.FRAME, width=30)
    input_entry.pack()

    # TODO temporaneo
    # Pulsante per aggiungere il messaggio
    button = Button(self.FRAME, text="Aggiungi Messaggio", command=self.on_button_click)
    button.pack()

    self.log_text_field = log_text_field
    self.input_entry = input_entry
    
  def on_button_click(self):
    message = self.input_entry.get()
    self.add_logs(message)
    self.input_entry.delete(0, END)  # Cancella il testo nell'input field