from tkinter import * # in python 3.x this would be from tkinter import *
from tkinter.ttk import *


root = Tk()
root.geometry("600x480+400+120")

style = Style()

Style().configure("TButton", padding=6, relief="flat", background="#ccc")

style.map("B.TButton",
foreground=[('pressed', 'green'), ('active', 'blue'), ('!pressed', 'red')],
background=[('pressed', '!disabled', 'grey'), ('active', 'white')]
)


style.map("C.TButton",
foreground=[('pressed', 'red'), ('active', 'blue')],
background=[('pressed', '!disabled', 'green'), ('active', 'white')]
)


style.map("D.TButton",
foreground=[('pressed', 'brown'), ('active', 'blue'), ('!pressed', 'green')],
background=[('pressed', '!disabled', 'grey'), ('active', 'white')]
)


style.map("E.TButton",
foreground=[('pressed', 'yellow'), ('active', 'purple'), ('!pressed', 'blue')],
background=[('pressed', '!disabled', 'grey'), ('active', 'white')]
)


# String variables and their initial text
myTextx=StringVar()
myTexty=StringVar()
myTextx.set("Hello")
myTexty.set("World")


# update of content of strings when mouse clicked within frame
def callback(event):
  myTextx.set(event.x)
  myTexty.set(event.y)


def hello():
  print ("hello!")


  # click mouse button inside this frame to update values in myTextx and myTexty ( not on buttons within frame )
  frame = Frame(root, width=500, height=300, relief=RAISED, borderwidth=5)
  frame.bind("<Button-1>", callback)
  frame.pack()

  btn = Button(text="Sample")
  btn.pack()

  colored_btn = Button(text="Test", style="C.TButton").pack(padx=45, pady=5)
  btn1 = Button(text="Hello").pack()

  #click btn2 to close program - using the quit command
  btn2 = Button(text="Goodbye", style="B.TButton", command=quit).pack(padx=45, pady=5)


  redbutton = Button(frame, text="Red", style="B.TButton")
  redbutton.pack(side = LEFT , padx=5, pady=25)


  greenbutton = Button(frame, text="Green", style="D.TButton")
  greenbutton.pack(side = LEFT ,padx=5, pady=25 )


  bluebutton = Button(frame, text="Blue", style="E.TButton")
  bluebutton.pack( side = LEFT , padx=5, pady=25)


  # values updated automatically
  w = Label(root, textvariable=myTextx).pack()
  x = Label(root, textvariable=myTexty).pack()


  listbox = Listbox(root)
  listbox.insert(END, "a list entry")

  for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)


    listbox.pack()


  # create a toplevel menu
  menubar = Menu(root)
  menubar.add_command(label="Hello!", command=hello)
  menubar.add_command(label="Quit!", command=root.quit)


  # display the menu
  root.config(menu=menubar)


  root.mainloop()
  

hello()