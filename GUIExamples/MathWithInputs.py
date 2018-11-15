import tkinter as tk

def submit():

	a = float(enta.get()) 
	b = float(entb.get())

	v = (a + b)/2
	v = round(v,3) 

	output.config(state="normal")

	outputValue = v

	output.delete(1.0,tk.END)
	output.insert(tk.INSERT,outputValue)
	output.config(state="disabled")

root = tk.Tk()
root.title("The Average of Two Numbers")

labr = tk.Label(root, text="Input 1 (Number)") 
labr.pack() 

enta = tk.Entry(root) 
enta.pack()

labh = tk.Label(root, text="Input 2 (Number)")  
labh.pack()

entb = tk.Entry(root)
entb.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=40, height=10, borderwidth=4, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()


root.mainloop()
