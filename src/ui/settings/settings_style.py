from tkinter.ttk import Style

""" Ttk represents the python library with graphic improvements compared to the
  Tkinter library, and to configure the style of the components contained in ttk
  we must use the Style class.

  This function configures all the default styles of the various widgets
  and the custom styles, which must be specified when creating the widget
  via the style='custom.style' property
"""
main_color = "#70878d"
secondary_color = '#FF6B00'
gray = '#626d75'
text_color = "#F7F7F7"

def configure_style():
  style = Style()
  
  # configure default styles
  style.configure("TCheckbutton", font=('Verdana', 11), foreground=text_color, background=main_color)
  style.configure("TLabel", font=('Verdana', 11), background=main_color, foreground=text_color)
  style.configure("Title.TLabel", font=('Verdana', 14, 'bold'), padding=(0,11), background=main_color, foreground=text_color)
  style.configure('TFrame', background=main_color)
  style.configure('TRadiobutton', font=('Verdana', 11), foreground=text_color, background=main_color)
  
  # card style
  # style.configure('Card.TFrame', background=card_color)
  # style.configure("CardTitle.TLabel", font=('Verdana', 14, 'bold'), background=card_color, padding=(0,11))
  
  # messageboxes style
  style.configure("MsgBoxTitle.TLabel", font=('Verdana', 25, 'bold'), background=main_color, foreground=text_color, padding=(0,13), justify="center")
  style.configure("MsgBoxSubtitle.TLabel", font=('Verdana', 11), background=main_color, foreground=text_color, justify="center")
  style.configure("MsgBoxTitle.TCheckbutton", font=('Verdana', 11), foreground=text_color, background=main_color)