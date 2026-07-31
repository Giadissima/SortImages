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
  style.theme_use('clam') # clam fully honors custom colors, unlike Windows' native theme

  # configure default styles
  style.configure("TCheckbutton", font=('Verdana', 11), foreground=text_color, background=main_color)
  style.configure("TLabel", font=('Verdana', 11), background=main_color, foreground=text_color)
  style.configure("Title.TLabel", font=('Verdana', 14, 'bold'), padding=(0,11), background=main_color, foreground=text_color)
  style.configure('TFrame', background=main_color)
  style.configure('TRadiobutton', font=('Verdana', 11), foreground=text_color, background=main_color)

  # keep hover/active state readable instead of falling back to clam's default white highlight
  style.map("TCheckbutton", background=[('active', gray)], foreground=[('active', text_color)])
  style.map("TRadiobutton", background=[('active', gray)], foreground=[('active', text_color)])

  # card style
  # style.configure('Card.TFrame', background=card_color)
  # style.configure("CardTitle.TLabel", font=('Verdana', 14, 'bold'), background=card_color, padding=(0,11))
  
  # messageboxes style
  style.configure("MsgBoxTitle.TLabel", font=('Verdana', 25, 'bold'), background=main_color, foreground=text_color, padding=(0,13), justify="center")
  style.configure("MsgBoxSubtitle.TLabel", font=('Verdana', 11), background=main_color, foreground=text_color, justify="center")
  style.configure("MsgBoxTitle.TCheckbutton", font=('Verdana', 11), foreground=text_color, background=main_color)
  style.map("MsgBoxTitle.TCheckbutton", background=[('active', gray)], foreground=[('active', text_color)])

  # main call-to-action button
  style.configure("Start.TButton", font=('Verdana', 12, 'bold'), foreground=text_color,
                  background=secondary_color, borderwidth=0, focuscolor='none', padding=(10, 4), width=8)
  style.map("Start.TButton", background=[('active', '#e65c00'), ('pressed', '#cc5200')])

  # secondary action button (pause/resume)
  style.configure("Pause.TButton", font=('Verdana', 12, 'bold'), foreground=text_color,
                  background='#5a636a', borderwidth=0, focuscolor='none', padding=(10, 4), width=8)
  style.map("Pause.TButton",
            background=[('disabled', '#9aa4a8'), ('active', '#4f575d'), ('pressed', '#3f464b')],
            foreground=[('disabled', text_color), ('active', text_color), ('pressed', text_color)])

  # progress bar (file scan progress)
  style.configure("TProgressbar", troughcolor=gray, background=secondary_color, bordercolor=main_color,
                  lightcolor=secondary_color, darkcolor=secondary_color)