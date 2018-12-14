import tkinter as tk

#With the login page, all elements are vertically aligned, so I just need to use pack

root=tk.Tk()

#If a function is written with a capital letter it indicates it is a constructor


#*********************Widget 1********************
#1. Construct the Object: We build and configure
#2. Configure the Object: We specify bheaviours and settings (OPTIONAL)
#3. Pack the Object: Put it in the window
labUN = tk.Label(root, text = "User Name")
#Ordered Parameters: The order we send them matters. (COMMON)
#Named Parameters: JavaScript and Python Specific
labUN.pack()

entUN = tk.Entry(root, show="*")
entUN.pack()

labPassword = tk.Label(root, text="Password")
labPassword.pack()

entPassword = tk.Entry(root)
entPassword.pack()

submit = tk.Button(root, text ="Submit", background="red")
submit.pack()

root.mainloop()