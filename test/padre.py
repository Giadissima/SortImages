import tkinter.ttk as ttk
import tkinter as tk

root = tk.Tk()
root.title("Frame padre")
root.geometry("1600x800")
root.configure(bg='#2A2A2A')


title = ttk.Label(root, text="Sort Images", background='red')
subframe = ttk.Label(root, text='sub frame', background='green')
btn = ttk.Button(root, text="Start")
log = ttk.Label(root, text="Logs", background='yellow')

title.pack(side='top', ipady=40, ipadx=60)
subframe.pack(pady=20, fill='y', expand=True)
log.pack(side='bottom',fill='x', ipady=100)
btn.pack(side='bottom', ipady=40, ipadx=60)
root.mainloop()