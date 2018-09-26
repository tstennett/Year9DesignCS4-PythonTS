import tkinter as tk
import math

def submit():
	#does something once submit button is pressed
	print("Submit pressed")
	r = float(entr.get()) #gets what's in the entry box and makes it a float
	h = float(enth.get())

	v = math.pi*r*r*h
	v = round(v,3) #rounds volume to 3 decimal places

	output.config(state="normal")
	output.insert(tk.INSERT,v) #inserts it in location
	output.config(state="disabled")

root = tk.Tk()
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="Radius") #makes labr a label
labr.pack() #constructs then packs

entr = tk.Entry(root) #an entry that takes whatever is typed in it
entr.pack()

labh = tk.Label(root, text="Height")  #label
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=20, height=15, borderwidth=4, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()


root.mainloop()

