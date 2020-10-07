from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Look! I clicked a button")
	myLabel.grid()
	print(e.get())


#first defining the widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Sreeram")
myButton = Button(root, text="Enter your name", padx=50, pady=50, command=myClick)
e = Entry(root)
e.grid()
e.insert(1,"Insert your name")


myLabel1.grid(row=0, column = 0)
myLabel2.grid(row=3, column = 1)

myButton.grid()



#creating an event loop,  it's looping and figures out any change
root.mainloop()