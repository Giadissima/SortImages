from tkinter import *
from tkinter import ttk
from PIL import Image

root = Tk()
root.title("Sort Image")
root.geometry("600x700")
root.configure(bg="red")
root.iconbitmap('icon.ico')
title = ttk.Label(root, text="Sort Image", font='Helvetica 20 bold', padding=10)
title.pack()

optionFrame = ttk.Frame(root, padding=10)

print(ttk.Frame(root, padding=10).configure())

btn = ttk.Button(root, text="Inizia", command=root.destroy)
btn.pack()
root.mainloop()