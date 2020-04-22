from tkinter import *
from tkinter import filedialog
import os


def createNewWindow(size):
    newWindow = Toplevel(root)


def print_on_window(value):
   mylist.insert(END, str(value))


def print_size_on_window(size):
    mylist.insert(END, str("---------------------------------------------------------------------------------------"))
    print(size)

    if size > 1000000000:
        mylist.insert(END, str(f"Directory size:  {round(size*1e-9, 2)} GB"))
    elif size > 100000:
        mylist.insert(END, str(f"Directory size: {round(size*0.000001, 2)} MB"))
    else:
        mylist.insert(END, str(f"Directory size: {size} Bytes"))
    mylist.insert(END, str("---------------------------------------------------------------------------------------"))
    mylist.yview(END)


def browse_button():
    directory = filedialog.askdirectory()
    total_size = 0.0
    start_path = '.'  # To get size of current directory
    for path, dirs, files in os.walk(directory):
        print(path, dirs, files)
        for f in files:
            print_on_window(f)
            fp = os.path.join(path, f)
            print(fp)
            total_size += os.path.getsize(fp)
    print(f"Directory size: {total_size} Bytes or {round(total_size*0.000001, 2)} MB or {round(total_size*1e-9, 2)} GB")
    print_size_on_window(total_size)


root = Tk()
root.geometry("600x400")
root.title("Directory Size Finder")
button_browse = Button(text="Browse", command=browse_button, font=("Arial", 11))
button_browse.pack()

scrollbar = Scrollbar(root)

scrollbar.pack(side = RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand = scrollbar.set, height = 100, font=("Arial", 11))
mylist.pack(fill=BOTH)

scrollbar.config(command = mylist.yview)

root.mainloop()
