import tkinter as tk
root = tk.Tk()
root.title("GUI Button")

def pressed(e):
	print("success")

btn = tk.Button(text="Press Me")
btn.bind("<Button>", pressed)
btn.pack()

root.mainloop()