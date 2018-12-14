#import matplotlib.pyplot as plt
#import tkinter as tk

#plt.figure(1, figsize=(3, 3))
#plt.plot(["Day 1","Day 2","Day 3","Day 4", "Day 5"],[1,2,3,8,9],'ro')
#plt.suptitle('Average Sleeping Hours')
#plt.show()

#names = ['group_a', 'group_b', 'group_c']
#plt.figure(1, figsize=(9, 3))
#plt.plot(["Day 1","Day 2","Day 3","Day 4"],[1,2,3,8],'ro')
#plt.suptitle('Categorical Plotting')
#plt.show()


#---------------------------------

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy
import pandas as pd

root = tk.Tk()
# plot the data itself
x = [1,2,5]
y = [2,3,1]
scatA = Figure(figsize=(3,3), dpi=106)
pylab = scatA.add_subplot(111)
pylab.plot(x,y,'ro')
# calc the trendline (it is simply a linear fitting)
z = numpy.polyfit(x, y, 1)
p = numpy.poly1d(z)
pylab.plot(x,p(x),'r–')

root.mainloop()