from cProfile import label
import code
from tkinter import*
from tkinter import font
import tkinter.messagebox
from tkinter.tix import COLUMN


def slider(value):
    r = red_Scale.get()
    g = green_Scale.get()
    b = blue_Scale.get()

    rgb = f'{r},{g},{b}'
    code = "#%02x%02x%02x" % (r, g, b)
    colorLabel.config(bg=code)
    rgb_entry.delete(0, END)
    rgb_entry.insert(0, rgb)


def oneClick():
    tkinter.messagebox.showinfo("Copy To Clipboard ", "your rgb color code  ("+rgb_entry.get()+")is copied")
    clip = Tk()
    clip.withdraw()
    clip.Clipboard_clear()
    clip.Clipboard_append(rgb_entry.get())
    clip.destory()


root = Tk()

root.title("color Picker")
root.geometry("360x380+100+100")
colorLabel = Label(root, bg="black", width=50, height=10, bd=1, relief=None)
colorLabel.pack(pady=5)
frame = Frame(root, bd=1, relief=None)
frame.pack(pady=5)

red_label = label(frame, text="red", fg="red",  font=("times new roman", 12, "bold"))
red_label.grid(row=0, COLUMN=0)
red_Scale = Scale(frame, from_=0, to=255, length=210, fg="red", orient=HORIZONTAL, command=slider)
red_Scale.grid(row=0, COLUMN=0)


green_label = label(frame, text="green", fg="green", font=("times new roman", 12, "bold"))
green_label.grid(row=1, COLUMN=0)
green_Scale = Scale(frame, from_=0, to=255, length=210, fg="green", orient=HORIZONTAL, command=slider)
green_Scale.grid(row=1, COLUMN=1)


blue_label = label(frame, text="blue", fg="blue", font=("times new roman", 12, "bold"))
blue_label.grid(row=2, COLUMN=0)
blue_Scale = Scale(frame, from_=0, to=255, length=210, fg="blue", orient=HORIZONTAL, command=slider)
blue_Scale.grid(row=2, COLUMN=1)

frame2 = Frame(root, bd=1, relief=None)
frame2.pack(pody=5)


rgb_label = label(frame2, text="rgb code:", font=("times new roman", 12, "bold"))
rgb_label.grid(row=2, COLUMN=0)
rgb_entry = Entry(frame2, width=12, font=("times new roman", 12))
rgb_entry.grid(row=2, column=1, padx=5)
rgb_entry.insert(END, '')

copy = Button(frame2, text="copy", font=( "times new roman", 12, "bold"), command=oneClick)
copy.grid(row=3, columnspan=2, pady=7)
root.mainloop()
