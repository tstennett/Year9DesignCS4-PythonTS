import tkinter as tk 

root = tk.Tk()

label = tk.Label(root, text="Title")
label.grid(row=1,column = 0,columnspan=5)

label1 = tk.Label(root, text="Label")
label1.grid(row = 3, column = 0, columnspan = 2)

root.mainloop()