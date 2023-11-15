import tkinter as tk

def cambia_colore():
    testo.delete(1.0, tk.END)  # Cancella il testo attuale nella casella di testo

    # Aggiungi la prima riga con il colore del font rosso
    testo.insert(tk.END, "Questa è la prima riga\n", 'rosso')

    # Aggiungi la seconda riga con il colore del font nero
    testo.insert(tk.END, "Questa è la seconda riga", 'nero')

# Crea la finestra principale
root = tk.Tk()
root.title("Esempio di cambio colore del testo")

# Crea una casella di testo
testo = tk.Text(root)
testo.pack()

# Configura il tag per il colore rosso
testo.tag_configure('rosso', foreground='red')

# Configura il tag per il colore nero
testo.tag_configure('nero', foreground='black')

# Crea un pulsante per cambiare il colore del testo
pulsante = tk.Button(root, text="Cambia Colore", command=cambia_colore)
pulsante.pack()

# Avvia il loop principale
root.mainloop()
