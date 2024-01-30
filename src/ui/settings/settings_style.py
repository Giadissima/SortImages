from tkinter.ttk import Style

""" Ttk represents the python library with graphic improvements compared to the
  Tkinter library, and to configure the style of the components contained in ttk
  we must use the Style class.

  This function configures all the default styles of the various widgets
  and the custom styles, which must be specified when creating the widget
  via the style='custom.style' property
"""
main_color = '#2A2A2A'
secondary_color = '#FF6B00'
gray = '#474747'
card_color = '#E5E5E5'

def configure_style():
  style = Style()
  
  # configure default styles
  style.configure("TCheckbutton", font=('Verdana', 11), background=card_color)
  style.configure("TLabel", font=('Verdana', 11), background=card_color)
  style.configure('TFrame', background=main_color)
  style.configure('TRadiobutton', font=('Verdana', 11), background=card_color)
  style.configure('Card.TFrame', background=card_color)
  
  # messageboxes style
  style.configure("MsgBoxTitle.TLabel", font=('Verdana', 25, 'bold'), background=main_color, foreground='white', padding=(0,13), justify="center")
  style.configure("MsgBoxSubtitle.TLabel", font=('Verdana', 11), background=main_color, foreground='white', justify="center")
  style.configure("MsgBoxTitle.TCheckbutton", font=('Verdana', 11), foreground='white', background=main_color)
  
  #subtitle style
  style.configure("CardTitle.TLabel", font=('Verdana', 15, 'bold'), background=card_color, padding=(0,13))