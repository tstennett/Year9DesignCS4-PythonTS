import tkinter as tk

root = tk.Tk() #Tk() is special method called constructor, only called once and it sets everything up for us

lab = tk.Label(root, text = "Enter a number:")
#To pack an element using the grid gemoetry manager, we use <object>.grid(parameters)

lab.grid(row = 0, column = 0)

ent = tk.Entry(root)
ent.grid(row = 1, column = 0)

btn = tk.Button(root, text = "Press me")
btn.grid(row = 2, column = 0)

output = tk.Text(root)
output.configure(state = "disable")
output.grid(row = 0, column = 1, rowspan = 2)



root.mainloop()