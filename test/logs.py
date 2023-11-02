from tkinter import *

def add_logs():
  path_entry.insert("ciao")

master = Tk()
path_entry = Entry(master)
add_logs()
mainloop()