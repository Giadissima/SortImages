from tkinter import BOTH, Frame, Tk, messagebox
from tkinter.ttk import Label, Button, Style

from src.sort import start_sort
from src.ui.option import create_opt_frame
from src.ui.folder_selection import create_selection_folder_frame
from src.ui.log import Logs
from src.config import Config
from src.ui.custom_messagebox import CustomMessageBox

# TODO implementa una conferma dell'utente prima di eseguire azioni irreversibili come l'eliminazione di cartelle
# TODO msgbox con don't show me again
class Interface():
  def __init__(self, title: str, size: str, icon_path: str, default_font = None, default_font_size = None):
    self.TITLE = title
    self.SIZE = size
    self.icon_path = icon_path
    self.default_font = default_font
    self.default_font_size = default_font_size
    self.root: Tk = Tk()
    self.config = Config()
    
    self.main_frame()
    
  def main_frame(self):

    self.root.title(self.TITLE)
    self.root.geometry(self.SIZE)
    self.root.iconbitmap(self.icon_path)
    
    self.style = Style()

    Style().configure("TButton", padding=3, background="white")

    self.style.map("B.TButton",
    foreground=[('pressed', 'orange'), ('active', 'orange'), ('!pressed', 'red')],
    background=[('pressed', '!disabled', 'active', 'white')],
    font='Noto 10 bold'
    )
    
    title = Label(self.root, text=self.TITLE, font='Noto 16 bold', padding=10)
    title.pack()
    
    form_frame = Frame(self.root)
    form_frame.pack(expand=True, fill=BOTH)
    
    selection_folder_frame = Frame(form_frame)
    selection_folder_frame.grid(row=0, column=0, padx=10, sticky="nsew")
    self.path_entry = create_selection_folder_frame(selection_folder_frame, self.icon_path, self.default_font)
    
    option_frame = Frame(form_frame)
    create_opt_frame(option_frame, self.default_font)
    option_frame.grid(row=0, column=1, sticky="nsew", padx=10)
    
    form_frame.columnconfigure(0, weight=1)  # Imposta il peso della colonna 0
    form_frame.columnconfigure(1, weight=1)  # Imposta il peso della colonna 1
    form_frame.rowconfigure(0, weight=1)     # Imposta il peso della riga 0
 
    btn = Button(self.root, text="Start", style="B.TButton", command=self.start_sort)
    btn.pack(pady=10)
    
    self.config.set_logs_obj(Logs(self.root))
    self.root.mainloop()
    
  def start_sort(self):
    if(Config.checkbox_choises[1].get() == 1):
      custom_message_box = CustomMessageBox(
        self.root,
        "Warning",
        "This operation will delete empty folders. Continue?",
        "Don't show again",
        icon=self.icon_path,
        style=self.style
      )
      self.root.wait_window(custom_message_box)  # Attendi che la finestra di dialogo venga chiusa

      print(custom_message_box)
      if custom_message_box.checkbox_var.get():
        print("Checkbox selezionata. Salva la preferenza qui.")
        #TODO
      
    self.config.set_input_folder(self.path_entry[0].get())
    self.config.set_output_folder(self.path_entry[1].get())
    result, msg = start_sort()
    if result: messagebox.showinfo(title="Success", message="Sort completed")
    else: messagebox.showerror(title="error", message=msg)
