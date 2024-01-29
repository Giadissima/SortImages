import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("300x200")
window.title("PythonExamples.org")

# Create a variable to hold the selected option
radio_var = tk.StringVar(value="Option 1")

# Create Radiobuttons
radio_button1 = tk.Radiobutton(window, text="Option 1", variable=radio_var, value="Option 1")
radio_button2 = tk.Radiobutton(window, text="Option 2", variable=radio_var, value="Option 2")
radio_button3 = tk.Radiobutton(window, text="Option 3", variable=radio_var, value="Option 3")

# Pack the Radiobuttons
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

# Start the Tkinter event loop
window.mainloop()