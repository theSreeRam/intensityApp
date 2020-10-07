from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('DOP PROJECT')


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="./", title="Select a file to upload")
    print(root.filename)
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command = open).pack()



root.mainloop()
