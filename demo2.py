from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('DOP Intensity calculator')
root.geometry("900x500")

lbl1 = Label(root, text="RGB Intensity Calculator",  font="none 24 bold")
lbl1.grid(row=0, column=0)


lbl1.place(anchor=N)
lbl1.grid(column=0, row=0)


# images = []

# root.filename =[]

# i=0 
# j=0

# def add():
# 	global my_image2
# 	added_button = Button()
# 	root.filename.append(filedialog.askopenfilename(initialdir="./", title="Select a file to upload"))


# def open():
#     global my_image
#     root.filename.append(filedialog.askopenfilename(initialdir="./", title="Select a file to upload"))
#     print(root.filename[0])
#     my_label = Label(root, text=root.filename[0]).grid()
#     my_image = ImageTk.PhotoImage(Image.open(root.filename[0]))
#     my_image_label = Label(image=my_image).grid()


# my_btn = Button(root, text="Open File", command = open).grid()



# insert = Button(root, text="Add Image", command=add).grid()

r=5

inputs = []
buttons = []
my_image = []
conc =[]
def open():
    curr = filedialog.askopenfilename()
    image = Image.open(curr)
    image = image.resize((100, 100), Image.ANTIALIAS) 
    global my_image,r
    my_label = Label(root, text=curr).grid(row=r, column=0)
    r+=1
    my_image.append(ImageTk.PhotoImage(image))
    my_image_label = Label(image=my_image[-1]).grid(row=r, column=0)
    r+=1
    inputs.append(curr)

def add():
	global r
	buttons.append(Button(root, text="Open", command=open).grid(row=r))
	r+=1
	current_conc = Entry(root)
	conc.append(current_conc)
	current_conc.grid(row=r)
	r+=3
	

insert = Button(root, text="Add Input Row", command=add).grid(row=3, column=0)

def submit():
    for idx in range(len(inputs)):
    	x = inputs[idx]
    	im = Image.open(x)
    	width,height = im.size
    	R=0
    	G=0
    	B=0
    	for x in list(im.getdata()):
    		R += x[0]
    		G += x[1]
    		B += x[2]
    	R /= (width*height)
    	G /= (width*height)
    	B /= (width*height)
    	print("concentration : " , conc[idx].get())
    	# print("conc = " , conc[idx])
    	print("RGB average :", (R+G+B)/3)


submit = Button(root, text="Calculate", command=submit).grid(row=3, column=3)


root.mainloop()