import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Image Example")
window.geometry("500x368")
window.configure(background='grey')

path = "image/emoji.jpg"

img = ImageTk.PhotoImage(Image.open(path))

panel = tk.Label(window, image = img)

panel.pack(side = "bottom", fill = "both", expand = "yes")

window.mainloop()