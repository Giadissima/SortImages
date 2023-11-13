from tkinter import *

def add_logs(index, message):
    log_text.config(state=NORMAL)  # Abilita la modifica del testo
    log_text.insert(END, f"{index}. {message}\n")
    log_text.config(state=DISABLED)  # Disabilita la modifica del testo

def on_button_click():
    global index
    message = input_entry.get()
    add_logs(index, message)
    index += 1
    input_entry.delete(0, END)  # Cancella il testo nell'input field

index = 1

master = Tk()
master.title("Finestra di Log")

# Finestra di log
log_text = Text(master, height=10, width=30, state=DISABLED)
log_text.pack()

# Input field
input_entry = Entry(master, width=30)
input_entry.pack()

# Pulsante per aggiungere il messaggio
button = Button(master, text="Aggiungi Messaggio", command=on_button_click)
button.pack()

mainloop()
