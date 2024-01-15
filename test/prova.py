import tkinter as tk
from PIL import Image, ImageTk, ImageFilter

def create_blurred_shadow_text(canvas, x, y, text, font, text_color, shadow_color, shadow_offset, blur_radius):
    # Creare un'immagine per il testo
    text_image = Image.new("RGBA", (canvas.winfo_reqwidth(), canvas.winfo_reqheight()), (0, 0, 0, 0))
    text_draw = ImageTk.PhotoImage(master=text_image)

    # Disegnare il testo sull'immagine
    canvas.create_text(x + shadow_offset, y + shadow_offset, text=text, font=font, fill=shadow_color, anchor='nw', image=text_draw)

    # Applicare la sfocatura all'ombra
    text_image_blurred = text_image.filter(ImageFilter.GaussianBlur(blur_radius))

    # Convertire l'immagine sfocata in un formato utilizzabile da Tkinter
    text_image_blurred_tk = ImageTk.PhotoImage(text_image_blurred)

    # Disegnare l'immagine sfocata sul Canvas
    canvas.create_image(x, y, anchor='nw', image=text_image_blurred_tk)

    # Creare il testo principale
    canvas.create_text(x, y, text=text, font=font, fill=text_color)

# Creare la finestra principale
root = tk.Tk()
root.title("Testo con Ombra Sfocata")

# Creare un Canvas
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

# Impostare le variabili
text = "Hello, Shadow!"
font = ("Helvetica", 20)
text_color = "blue"
shadow_color = "gray"
shadow_offset = 5
blur_radius = 3  # Puoi regolare il raggio della sfocatura

# Creare il testo con ombra sfocata
create_blurred_shadow_text(canvas, 100, 100, text, font, text_color, shadow_color, shadow_offset, blur_radius)

# Avviare il loop della finestra
root.mainloop()
