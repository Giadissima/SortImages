from tkinter import BOTH, Frame, Tk, messagebox
from tkinter.ttk import Label, Button, Style

from src.sort import start_sort
from src.ui.option import create_opt_frame
from src.ui.folder_selection import create_selection_folder_frame
from src.ui.log import Logs
from src.config import Config
from src.ui.custom_messagebox import CustomMessageBox

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
    # TODO trasformare il tutto in una funzione con array associativi per le preferenze
    if(Config.checkbox_choises[0].get() == 1 and not self.find_preference("DUPLICATES_CHOISE")):
      msg = "The program will delete duplicate images.\nIt will not be possible to recover them.\nContinue?"
      custom_message_box_1 = self.ask_to_custom_msgbox(msg, "DUPLICATES_CHOISE")
      if not custom_message_box_1: return
    
    if(Config.checkbox_choises[1].get() == 1 and not self.find_preference("FOLDERS_CHOISE")):  
      msg = "Are you sure you want to delete empty folders\nfrom the starting folder?"
      custom_message_box_2 = self.ask_to_custom_msgbox(msg, "FOLDERS_CHOISE")
      if not custom_message_box_2: return
   
    self.config.set_input_folder(self.path_entry[0].get())
    self.config.set_output_folder(self.path_entry[1].get())
    result, msg = start_sort()
    if result: messagebox.showinfo(title="Success", message="Sort completed")
    else: messagebox.showerror(title="error", message=msg)

  def ask_to_custom_msgbox(self, message, choise_name, title='Warning'):
    custom_message_box = CustomMessageBox(
      self.root,
      title,
      message,
      icon=self.icon_path
    )
    self.root.wait_window(custom_message_box)  # Attendi che la finestra di dialogo venga chiusa

    if custom_message_box.checkbox_var.get():
      print("Checkbox selezionata. Salva la preferenza qui.")
      with open('config.ini', "a+") as f:
        f.write(f'{choise_name}=True')
        f.write('\n')

    if(custom_message_box.ok):
      return True
    return False
  
  def find_preference(self, preference):
    try:
      with open('config.ini', 'r') as file:
        for line_number, line in enumerate(file, start=1):
          print(line)
          if f'{preference}=True' in line:
              print(f"Trova 'DUPLICATE_IMG' alla riga {line_number}: {line.strip()}")
              # Puoi fare altre operazioni qui se necessario
              return True  # Trovato, esci dalla funzione
    except FileNotFoundError:
        print(f"Il file 'config.ini' non esiste.")
        return False