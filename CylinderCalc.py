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

	outputValue = "Given\nradius: " +str(r) + " units\nheight "+str(h)+" units\nThe volume is: "+str(v)+" units cubed\n"

	output.delete(1.0,tk.END)
	output.insert(tk.INSERT,outputValue) #inserts it in location
	output.config(state="disabled")

root = tk.Tk()
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="Radius", background = "red") #makes labr a label
labr.pack() #constructs then packs

entr = tk.Entry(root, background = "orange") #an entry that takes whatever is typed in it
entr.pack()

labh = tk.Label(root, text="Height", background = "yellow")  #label
labh.pack()

enth = tk.Entry(root, background = "green")
enth.pack()

#we bind a function to a key
btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=40, height=10, borderwidth=4, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()


root.mainloop()

