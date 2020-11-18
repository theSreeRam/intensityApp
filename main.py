from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import ttk

root = Tk()


root.title('DOP Intensity calculator')
root.geometry("900x500")

#create a MAIN FRAME
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

#Create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

#add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

#configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

#create another frame inside the canvas
second_frame = Frame(my_canvas)

#add that new frame to a window in the canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")



lbl1 = Label(second_frame, text="RGB Intensity Calculator",  font="none 24 bold")
lbl1.grid(row=0, column=0)


lbl1.place(anchor=N)
lbl1.grid(column=0, row=0)


# images = []

# second_frame.filename =[]

# i=0 
# j=0

# def add():
# 	global my_image2
# 	added_button = Button()
# 	second_frame.filename.append(filedialog.askopenfilename(initialdir="./", title="Select a file to upload"))


# def open():
#     global my_image
#     second_frame.filename.append(filedialog.askopenfilename(initialdir="./", title="Select a file to upload"))
#     print(second_frame.filename[0])
#     my_label = Label(second_frame, text=second_frame.filename[0]).grid()
#     my_image = ImageTk.PhotoImage(Image.open(second_frame.filename[0]))
#     my_image_label = Label(image=my_image).grid()


# my_btn = Button(second_frame, text="Open File", command = open).grid()



# insert = Button(second_frame, text="Add Image", command=add).grid()

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
    my_label = Label(second_frame, text=curr).grid(row=r, column=0)
    r+=1
    my_image.append(ImageTk.PhotoImage(image))
    my_image_label = Label(second_frame, image=my_image[-1]).grid(row=r, column=0)
    r+=1
    inputs.append(curr)

def add():
	global r
	buttons.append(Button(second_frame, text="Open", command=open).grid(row=r))
	r+=1
	current_conc = Entry(second_frame)
	conc.append(current_conc)
	current_conc.grid(row=r)
	r+=3
	

insert = Button(second_frame, text="Add Input Row", command=add).grid(row=3, column=0)

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


submit = Button(second_frame, text="Calculate", command=submit).grid(row=3, column=3)


root.mainloop()