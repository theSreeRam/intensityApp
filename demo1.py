from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('DOP Intensity calculator')
root.geometry("900x500")


# def open():
# 	# global my_image
# 	root.filename = filedialog.askopenfilename(initialdir = "./" , title="Select image" , filetypes=(("png files", "*.png"), ("jpeg files" ,"*.jpeg"), ("all files", "*.*")))
# 	my_image = ImageTk.PhotoImage(Image.open(root.filename))
# 	my_image_label = Label(image = my_image).pack()

# my_btn = Button(root, text="Open Image", command=open).pack()

my_entries = []

def something():
	entry_list = ''

	for entries in my_entries:
		entry_list = entry_list + entries.get() + '\n'
		my_label.config(text= entry_list) 

	# print(my_entries[1].get())

my_entry = Entry(root)
my_entry.grid(row=0, column = 0, pady=20, padx=5)

#row loop
for y in range(5):
	#column loop
	for x in range(5):
		my_entry = Entry(root)
		my_entry.grid(row=y, column = x, pady=20, padx=5)
		my_entries.append(my_entry)

my_button = Button(root, text = "Click Me", command=something)
my_button.grid()

my_label = Label(root, text='')
my_label.grid()


root.mainloop()