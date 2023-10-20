from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Sort Image")
root.geometry("500x500")
ttk.Label(root, text="Hello World!").pack()
btn = ttk.Button(root, text="Quit", command=root.destroy)
btn.pack()
root.mainloop()