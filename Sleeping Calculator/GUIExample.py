import tkinter as tk

root = tk.Tk()
root.title('Steady State Data Processing')
root.geometry('{}x{}'.format(900, 500))


topFrame = tk.Frame(root, bg = 'lavender', width = 900, height=100, relief = 'raised') # , padx = 100, pady=100
topFrame.grid(row = 0, column = 0, columnspan = 3,  sticky="w")


labelCps = tk.Label(root, text='Cps', width = 0, height = 0, padx = 10, pady = 10) 
labelIgn = tk.Label(root, text='Ign', width = 0, height = 0, padx = 10, pady = 10) 
labelInj = tk.Label(root, text='Inj', width = 0, height = 0, padx = 10, pady = 10)


labelCps.grid(row = 1, column = 0, sticky='we')
labelIgn.grid(row = 1, column = 1, sticky='we')
labelInj.grid(row = 1, column = 2, sticky='we')
cpsFrame = tk.Frame(root, width = 300, height = 100, relief = 'raised') # , padx = 100, pady=100
cpsFrame.grid(row = 2, column = 0,  sticky="nsew")

ignFrame = tk.Frame(root, width = 300, height = 100, relief = 'raised') # , padx = 100, pady=100
ignFrame.grid(row = 2, column = 1,  sticky="nsew")

injFrame = tk.Frame(root, width = 300, height = 100, relief = 'raised') # , padx = 100, pady=100
injFrame.grid(row = 2, column = 2,  sticky="nsew")


labelAdv = tk.Label(cpsFrame, anchor = 'center', text='Cps adv threshold:') 
labelAdv.grid(row = 0, column = 0, sticky = 'w')

entryAdv = tk.Entry(cpsFrame)
entryAdv.grid(row = 0, column = 1, sticky = 'e')

labelIgn = tk.Label(ignFrame, justify = 'left', text = 'Dwell start threshold:') 
labelIgn.grid(row = 0, column = 0, sticky = 'w')
entryIgn = tk.Entry(ignFrame)
entryIgn.grid(row = 0, column = 1)
labelIgn = tk.Label(ignFrame, anchor = 'center', text = 'Dwell end threshold:') 
labelIgn.grid(row = 1, column = 0)
entryIgn = tk.Entry(ignFrame)
entryIgn.grid(row = 1, column = 1)

labelInj = tk.Label(injFrame, anchor = 'center', text = 'Inj start threshold:') 
labelInj.grid(row = 0, column = 0)
entryInj = tk.Entry(injFrame)
entryInj.grid(row = 0, column = 1)
labelInj = tk.Label(injFrame, anchor = 'center', text = 'Inj end threshold:') 
labelInj.grid(row = 1, column = 0)
entryInj = tk.Entry(injFrame)
entryInj.grid(row = 1, column = 1)

root.grid_rowconfigure(3, pad = 50)

applyButton = tk.Button(root, text = 'Apply', padx = 30, pady = 15)
applyButton.grid(row = 3, columnspan = 3)


text = ['Plot raw data', 'Plot tooth rpm', 'Plot cycle rpm', 'Plot ign data']
count = 0

for t in text:

    dataButton = tk.Button(root ,text = t, width = 5, height = 5 ,anchor = 'center', padx = 30, pady = 15)
    dataButton.grid(row = 4, column = count, sticky = 'news')
    # dataButton.grid_columnconfigure(count, weight = 2)    
    count = count + 1

root.mainloop()
