from tkinter.ttk import Style

def configure_style():
  style = Style()
  style.configure("TButton", padding=3, background="white")
  style.map("B.TButton",
                  foreground=[('pressed', 'orange'),
                              ('active', 'orange'), ('!pressed', 'red')],
                  background=[
                      ('pressed', '!disabled', 'active', 'white')],
                  font='Noto 10 bold')
  return style