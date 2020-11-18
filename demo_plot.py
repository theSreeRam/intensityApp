from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt


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
rgb_vals = []
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
		ave = (R+G+B)/3
		print("RGB average :", ave)
		rgb_vals.append(ave)
	# concentrations = list()
	# for idx in range(len(conc)-1):
		# concentrations.append(int(conc[idx].get()))
	# known_rgb_vals = rgb_vals[0:len(rgb_vals)-1]
	# unknown_rgb = rgb_vals[-1]
	# model = np.polyfit(known_rgb_vals, concentrations, 1)
	# print(model)
	# predict = np.poly1d(model)
	# print(predict(unknown_rgb))
	

def make_plot():
	rgbvals = list()
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
		ave = (R+G+B)/3
		rgbvals.append(ave)
	concentrations = list()
	for idx in range(len(conc)-1):
		concentrations.append(int(conc[idx].get()))
	known_rgb_vals = rgbvals[0:len(rgbvals)-1]
	unknown_rgb_val = rgbvals[-1];
	#print("Known RGB Values: ", known_rgb_vals)
	#print("Unknown RGB Value: ", unknown_rgb_val)
	model = np.polyfit(known_rgb_vals, concentrations, 1);
	predict = np.poly1d(model);
	unknown_conc = predict(unknown_rgb_val)
	print("Unknown Concentration: ", unknown_conc)
	plt.scatter(concentrations, known_rgb_vals, c='b', label='Known Samples')
	plt.scatter(unknown_conc, unknown_rgb_val, c='r', label='Unknown Sample');
	plt.ylabel("Average RGB Intensity")
	plt.xlabel("Concentration")
	plt.title("RGB Intensity vs Concentration")
	label = f"({round(unknown_conc,2)}, {round(unknown_rgb_val,2)})"
	
	
	x_lin_reg = list(concentrations);
	y_lin_reg = (x_lin_reg - model[1])/model[0]
	plt.plot(x_lin_reg,y_lin_reg, c='y', label='Best Fit Line')
	
	
	plt.annotate(label, (unknown_conc,unknown_rgb_val), textcoords="offset points", xytext=(10,-20), ha="center")
	for x,y in zip(concentrations, rgbvals):
		label = f"({x},{round(y,2)})"
		plt.annotate(label, (x,y),textcoords="offset points", xytext = (0,10), ha="center")
		plt.ylim(min(rgbvals)-15, max(rgbvals)+15)
	plt.legend(loc='upper left')
	plt.show()
	


submit = Button(root, text="Calculate", command=submit).grid(row=3, column=3)
submit = Button(root, text="Plot", command=make_plot).grid(row=4, column=3)


root.mainloop()
