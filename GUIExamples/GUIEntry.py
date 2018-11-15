import tkinter as tk

def run():
	str = entry.get()
	label.configure(text = str)

root = tk.Tk()

entry = tk.Entry(root)
entry.config(fg = "blue", text = "Entry Box")
entry.grid(column=2,row=1,columnspan=2)

button = tk.Button(root, text="Button", command=run)
button.grid(column=5,row=1,columnspan=1)

label = tk.Label(root,text="")
label.grid(row=2,column=2,columnspan=2)

root.mainloop()