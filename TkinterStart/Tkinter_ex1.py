#Tkinter Tutorial from http://effbot.org/tkinterbook/

#Hello, Tkinter

from Tkinter import *

root = Tk()		#set up the main window

#create a Label widget as a child to the root window
#Label widget can display text, an icon or other image.

w = Label(root, text="Hello, world!")	#In this case, we use the text option
#call the pack method on this widget
w.pack()	#pack size widget to fit the given text, and make it visible

root.mainloop()		#mainloop event shows the window (make it visible)

#The program will stay in the event loop until we close the window.