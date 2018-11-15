import tkinter as tk

def run():
	str = entry.get()
	output.config(state="normal")
	outputValue = str
	output.insert(tk.INSERT, outputValue)
	output.config(state="disabled")

root = tk.Tk()

entry = tk.Entry(root)
entry.config(fg = "blue", text = "Entry Box")
entry.grid(column=1,row=1,columnspan=2)

button = tk.Button(root, text="Button", command=run)
button.grid(column=3,row=1,columnspan=1)

output = tk.Text(root, height = 2, width=10, borderwidth=5, relief=tk.GROOVE)
output.grid(column= 2, row=2)
output.config(state="disabled")

root.mainloop()