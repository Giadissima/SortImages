from tkinter import BOTH, DISABLED, END, NORMAL, Text

class TkinterLogs():
  def __init__(self, frame) -> None:
    self.FRAME = frame
    self.log_text_field = Text(self.FRAME, height=10, width=30, state=DISABLED)
    self.log_text_field.tag_configure('error', foreground='red')
    self.log_text_field.tag_configure('info', foreground='blue')
    self.log_text_field.tag_configure('debug', foreground='black')
    self.log_text_field.pack(expand=True, fill=BOTH, padx=10, pady=10)
    
  def add_logs(self, message, tag):
    self.log_text_field.config(state=NORMAL)  # Abilita la modifica del testo
    self.log_text_field.insert(END, f"{message}\n", tag)
    self.log_text_field.config(state=DISABLED)  # Disabilita la modifica del testo
    self.log_text_field.see(END)
    
  def on_button_click(self):
    message = self.input_entry.get()
    self.add_logs(message)
    self.input_entry.delete(0, END)  # Cancella il testo nell'input field
    
  def delete_logs(self):
    self.log_text_field.config(state=NORMAL)  # Abilita la modifica del testo
    self.log_text_field.delete(1.0, END)  # Cancella tutto il testo nella casella di testo
    self.log_text_field.config(state=DISABLED)  # Disabilita la modifica del testo