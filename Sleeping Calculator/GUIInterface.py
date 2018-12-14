import tkinter as tk
from PIL import ImageTk, Image
import math
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()
root.configure()

#Allows only integers in to the entry box, courtesy of https://stackoverflow.com/questions/8959815/restricting-the-value-in-tkinter-entry-widget
def validate(action, index, value_if_allowed,prior_value, text, validation_type, trigger_type, widget_name):
    if text in '0123456789.':
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False
    else:
        return False

#end program button
def terminate():
	raise SystemExit

def submit():
	output1.config(state = "normal")
	output1.delete(1.0,'end')
	output1.config(state = "disable")
	output2.config(state = "normal")
	output2.delete(1.0,'end')
	output2.config(state = "disable")
	a = entry1.get() 
	b = entry2.get()
	c = entry3.get()
	d = entry4.get()
	e = entry5.get()

	a = float(a)
	b = float(b)
	c = float(c)
	d = float(d)
	e = float(e)

	#Using list to find the farthest numbers for sleep fluctuations
	list = [a,b,c,d,e]

	#Average part of output
	average = (a+b+c+d+e)/5
	inserttext1 = str(average) + " \nhours"
	output1.config(state = "normal")
	output1.insert(tk.INSERT, inserttext1)
	output1.config(state="disabled")

	#Line graph
	x = ["Day 1","Day 2", "Day 3", "Day 4", "Day 5"]
	y = [a,b,c,d,e]

	scatA = Figure(figsize=(3,3), dpi=106)
	scatB = scatA.add_subplot(111)
	scatB.plot(x,y)
	scatC = FigureCanvasTkAgg(scatA)
	scatC.get_tk_widget().grid(column = 4, columnspan = 5, row = 18, rowspan = 14)
        
	#Image
	if average >= 7.5:
		panel2.grid_remove()
		panel.grid()

	if average < 7.5:
		panel.grid_remove()
		panel2.grid()

	#Comments
	ma = max([a,b,c,d,e])
	mi = min([a,b,c,d,e])
	ma = int(ma)
	mi = int(mi)

	if abs(ma - mi) >= 5:
		global inserttext7
		global inserttext6
		global inserttext8
		inserttext6 = " Also, it is evident that your sleep fluctuates \ngreatly. Try to regulate your sleeping hours in order to ensure your body can adjust \nto your sleeping schedule."
		inserttext7 = " Also, it is evident that your \nsleep fluctuates greatly. Try to regulate your \nsleeping hours in order to ensure your body can adjust to your sleeping schedule."
		inserttext8 = "	Also, it is evident that your sleep fluctuates greatly. Try to regulate the amount of sleep you get, in order to ensure your body can adjust and function on a familiar sleeping amount."
	else:
		inserttext6 = ""
		inserttext7 = ""
		inserttext8 = ""

	if average <= 5:
		inserttext2 = "	Your sleep schedule is abysmal. \nStudies show this lack of sleep will \nresult in poor grades, and an overall \nreduction in production. To get better, \ntry organizing a specific schedule for your activities, allowing for atleast 7.5 hours of sleep. In order to properly facilitate \nthis sleep schedule, try slowly building up towards healthy sleeping hours. Ideally, \nyou should try to aim for 8-12 hours of \nsleep, as this will allow for good bodily \ndevelopment and a refreshed mind."
		output2.config(state = "normal")
		output2.insert(tk.INSERT, inserttext2)
		output2.insert(tk.INSERT, inserttext6)
		output2.config(state = "disabled")

	if average > 5 and average < 7.5:
		inserttext3 = "	Your sleep schedule is poor. \nIdeally, in order to be the healthiest, \nensure that you sleep atleast 7.5 hours a \nday. This ensures your body is refreshed \nand prepared to perform its functions \nproperly."
		output2.config(state = "normal")
		output2.insert(tk.INSERT, inserttext3)
		output2.insert(tk.INSERT, inserttext7)
		output2.config(state = "disabled")

	if average >= 7.5 and average <= 12 and abs(ma-mi) < 5:
		inserttext4 = "	Great job this week! Your healthy \nsleep schedule means that you are developing and can function at your body's desired \nrate. Continue the good work!"
		output2.config(state = "normal")
		output2.insert(tk.INSERT, inserttext4)
		output2.config(state = "disabled")

	if average >= 7.5 and average <= 12 and abs(ma-mi) > 5:
		inserttext4 = "	Great job mainting a good average sleep amount! Unfortunately, your sleep still flucatuates too much, so you should aim to have a regulated sleeping amount, in order to ensure your body can adjust to the sleeping hours."
		output2.config(state = "normal")
		output2.insert(tk.INSERT, inserttext4)
		output2.config(state = "disabled")

	if average > 12 and average <= 24:
		inserttext5 = "	Although your body will be healthy, your sleep schedule is very excess. Try to sleep in-between 7.5 to 12 hours, in order to be the most efficient."
		output2.config(state = "normal")
		output2.insert(tk.INSERT, inserttext5)
		output2.insert(tk.INSERT, inserttext8)
		output2.config(state = "disabled")
	
	if average > 24:
		inserttext9 = "	Please enter appropriate inputs, you can not sleep more than 24 hours."

def colourchange():
	global button_clicks
	button_clicks += 1
	if button_clicks%2==0:
		cbutton.config(image = c2photo)
		labeltitle.configure(background = '#00ACAC')
		label4input.configure(background = '#00F5EC')
		labelinput1.configure(background = '#00AEA7')
		labelinput2.configure(background = '#00AEA7')
		labelinput3.configure(background = '#00AEA7')
		labelinput4.configure(background = '#00AEA7')
		labelinput5.configure(background = '#00AEA7')
		imagetxt.configure(background = '#00F5EC')
		endtxt.configure(background = '#00F5EC')
		ctxt.configure(background = '#00F5EC')
		labeloutput1.configure(background ='#00F5EC')
		labeloutput2.configure(background ='#00F5EC')
		stext.configure(background ='#00F5EC')

	else:
		cbutton.config(image = c1photo)
		labeltitle.configure(background = '#FF8F2C')
		label4input.configure(background = '#FFBA7D')
		labelinput1.configure(background = '#FFA453')
		labelinput2.configure(background = '#FFA453')
		labelinput3.configure(background = '#FFA453')
		labelinput4.configure(background = '#FFA453')
		labelinput5.configure(background = '#FFA453') 
		imagetxt.configure(background = '#FFBA7D')
		endtxt.configure(background = '#FFBA7D')
		ctxt.configure(background = '#FFBA7D')
		labeloutput1.configure(background ='#FFBA7D')
		labeloutput2.configure(background ='#FFBA7D')
		stext.configure(background ='#FFBA7D')


#Main title
labeltitle = tk.Label(root, text = "Sleeping Calculator", font =("Helvetica bold",28), relief = 'raised', background = '#FF8F2C')
labeltitle.grid(column = 1, row = 0, columnspan = 8)

vcmd = (root.register(validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
#_________________________________________________________-

#Input subtitle
label4input = tk.Label(root, text = "Amount of Hours Asleep", font=("Helvetica bold", 18), padx = 5, relief = "raised")
label4input.configure(background = '#FFBA7D')
label4input.grid(column = 1, row = 2, rowspan=2, columnspan = 2, pady = 2)

#Input Day 1 
labelinput1 = tk.Label(root,text="Day 1",font=("Helvetica", 16), relief = 'groove', background = '#FFA453')
labelinput1.configure()
labelinput1.grid(column=1, row=4, columnspan =2)

entry1 = tk.Entry(root, width = 2,validate = 'key', validatecommand = vcmd)
entry1.configure(relief = 'ridge')
entry1.grid(column=1, row=5, columnspan =2, sticky = "new")

#Input Day 2
labelinput2 = tk.Label(root,text="Day 2",font=("Helvetica", 16), relief = 'groove', background = '#FFA453')
labelinput2.configure()
labelinput2.grid(column=1, row=6, columnspan =2)

entry2 = tk.Entry(root, width = 2,validate = 'key', validatecommand = vcmd)
entry2.configure(relief = 'ridge')
entry2.grid(column=1, row=7, columnspan =2, sticky = "new")

#Input Day 3
labelinput3 = tk.Label(root,text="Day 3",font=("Helvetica", 16), relief = 'groove', background = '#FFA453')
labelinput3.configure()
labelinput3.grid(column=1, row=8, columnspan =2)

entry3 = tk.Entry(root, width = 2,validate = 'key', validatecommand = vcmd)
entry3.configure(relief = 'ridge')
entry3.grid(column=1, row=9, columnspan =2, sticky = "new")

#Input Day 4
labelinput4 = tk.Label(root,text="Day 4",font=("Helvetica", 16), relief = 'groove', background = '#FFA453')
labelinput4.grid(column=1, row=10, columnspan =2)

entry4 = tk.Entry(root, width = 2,validate = 'key', validatecommand = vcmd)
entry4.configure(relief = 'ridge')
entry4.grid(column=1, row=12, columnspan =2, sticky = "new")

#Input Day 5
labelinput5 = tk.Label(root,text="Day 5",font=("Helvetica", 16), relief = 'groove', background = '#FFA453')
labelinput5.grid(column=1, row=13, columnspan =2)

entry5 = tk.Entry(root, width = 2,validate = 'key', validatecommand = vcmd)
entry5.configure(relief = 'ridge')
entry5.grid(column=1, row=14, columnspan =2, sticky = "new")

#Submit button
btn1 = tk.Button(root,text="Submit", font=("Helvetica bold", 16), relief = 'raised', width = 10, borderwidth = 2, command = submit)
btn1.configure(background = '#FD2C31') #Colour change is not working with buttons
btn1.grid(column =1, row = 15, columnspan = 2, pady = 5)

#_____________________________________________________________________

#Image Title
imagetxt = tk.Label(root, text = "Reward:",font=("Helvetica bold", 18), relief = 'raised', background = '#FFBA7D')
imagetxt.grid(row = 17, columnspan = 2, column = 1)

path = "image/emoji.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img, relief = 'ridge', borderwidth = 1, height = 90)
panel.grid(column = 1, columnspan = 2, row = 18, rowspan = 5, pady = 2)
panel.grid_remove()

path2 = "image/bad.png"
img2 = ImageTk.PhotoImage(Image.open(path2))
panel2 = tk.Label(root, image = img2, relief = 'ridge', borderwidth = 1, height = 90)
panel2.grid(column = 1, columnspan = 2, row = 18, rowspan = 5, pady = 2)
panel2.grid_remove()

#Terminate button
endtxt = tk.Label(root, text = "Close:", font =("Helvetica bold", 16), relief = 'raised',background = '#FFBA7D')
endtxt.grid(column = 1, columnspan = 2, row = 24)

end=tk.Button(root, command = terminate)
xphoto=tk.PhotoImage(file="image/x.ppm")
end.config(image=xphoto,width="35",height="35")
end.grid(column = 2, row = 25, sticky = 'w')

#Colour Change
ctxt = tk.Label(root, text = "Change Colours:",font=("Helvetica bold", 16), relief = 'raised', background = '#FFBA7D')
ctxt.grid(column = 1, columnspan = 2, row = 26)

cbutton = tk.Button(root, command = colourchange)
c1photo = tk.PhotoImage(file = "image/c1.ppm")
button_clicks = 1
cbutton.config(image = c1photo, width = "35", height = "35")
cbutton.grid(column = 2, row = 27, sticky = "w")
c2photo = tk.PhotoImage(file = "image/c2.ppm")
#_________________________________________________________________________________

#Output Box 1
labeloutput1 = tk.Label(root, text= "Average Hours Asleep:",font=("Helvetica bold", 18), relief = 'raised', background = '#FFBA7D')
labeloutput1.grid(column = 4, row = 3, rowspan = 2)

output1 = tk.Text(root, height = 2, width = 10, borderwidth = 2, relief = 'ridge')
output1.config(state= "disabled")
output1.grid(column = 5, row = 3, rowspan = 2, columnspan = 3, sticky= "nes", padx = 12)

#Output Box 2
labeloutput2 = tk.Label(root, text= "Comments:",font=("Helvetica bold", 18), relief = 'raised', background = '#FFBA7D')
labeloutput2.grid(column = 4, row = 6, columnspan = 1, sticky = 'w', padx = 2)

output2 = tk.Text(root, height = 8, width = 20, borderwidth = 2, relief = 'ridge')
output2.config(state="disabled")
output2.grid(column = 4, row = 7, columnspan = 5, rowspan = 9, sticky = 'nesw', padx = 2, pady = 5)

#_______________________________________________________________________

#Scattertext
stext = tk.Label(root, text= "Line Graph:",font=("Helvetica bold", 18), relief = 'raised', background = '#FFBA7D')
stext.grid(column = 4, row = 17, columnspan = 1, sticky = 'w', padx = 2, pady = 6)

#_______________________________________________________________________

#Makes the divider on the right side of the input boxes
separator1 = tk.Frame(bd=1, relief='sunken', width = 2, height = 346, background = 'black')
separator1.grid(column = 3, row = 2, rowspan = 15, padx = 5, sticky = "n")

#Makes divider on the top of input boxes
separator2 = tk.Frame(height=2, bd=1, relief='sunken', background = 'black')
separator2.grid(column = 1, row =1, sticky = "nesw", pady = 5, columnspan = 2, padx = 2)

#Makes divider on the top of output boxes
separator3 = tk.Frame(height=2, bd=1, relief='sunken', background = 'black')
separator3.grid(column = 3, columnspan = 5, row =1, sticky = "nesw", pady = 5, padx = 12)

#Makes divider under first output box
separator4 = tk.Frame(height=2, bd=1, relief='sunken', background = 'black')
separator4.grid(column = 3, columnspan = 5, row =5, sticky = "ew", pady = 7, padx = 12)

#Makes divider on bottom of inputs
separator5 = tk.Frame(height=2, bd=1, relief='sunken', background = 'black')
separator5.grid(column = 1, row =16, sticky = "ew", pady = 5, columnspan = 2, padx = 2)

#Makes the divider on the right side of the images
separator6 = tk.Frame(bd=1, relief='sunken', width = 2, height = 346, background = 'black')
separator6.grid(column = 3, row = 17, rowspan = 15, padx = 5, sticky = "n")

#Makes divider on the on the top of the scatterplot
separator7 = tk.Frame(height=2, bd=1, relief='sunken', background = 'black')
separator7.grid(column = 3, columnspan = 5, row =16, sticky = "ew", pady = 7, padx = 12)


root.mainloop()