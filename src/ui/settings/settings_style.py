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

def configure_style():
  style = Style()
  
  # configure default styles
  style.configure("TButton", padding=0, background="white")
  style.configure("TCheckbutton", font=('Noto', 11))
  style.configure("TLabel", font=('Inter', 11))
  
  style.configure('TFrame', background=main_color)
  
  # title style
  style.configure("Title.TLabel", font=('Noto', 22, 'bold'), padding=18, foreground='purple')
  
  #subtitle style
  style.configure("Subtitle.TLabel", font=('Noto', 11, 'bold'))