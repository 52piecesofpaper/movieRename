import inspect
import os
from tkinter import *
from tkinter import filedialog, messagebox

import PIL
from PIL import Image
from PIL import ImageTk

import read_write

import find_movies_in_dir

# root initialisation
root = Tk()
root.title('Organise Your Movies')
# root.geometry("800x600")
root.resizable(False, False)
root.configure(background='#e6ffe6')
img = ImageTk.PhotoImage(PIL.Image.open("icons8.png"))
root.iconphoto(True, img)

mainFolder = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


# Functions
def okay_button_click(search_directory):
    if os.path.exists(search_directory):
        find_movies_in_dir.find_movies_in_dir(search_directory)
        os.chdir(mainFolder)
        read_write.write_to_file(search_directory)
        # update_drop_down()
    else:
        messagebox.showerror("Error!", "Invalid directory")
    entry.delete(0, 'end')


def explore():
    dir_name = filedialog.askdirectory()
    entry.delete(0, 'end')
    entry.insert(0, str(dir_name))
    # read_write.write_to_file(str(dir_name))


# def update_drop_down():
#     drop.destroy()
#     print('hey')
#     new_history = read_write.read_files()
#     new_history.reverse()
#     new_clicked = StringVar()
#     new_clicked.set(history[0])
#     drop2 = OptionMenu(frame2, clicked, *history)
#     drop2.config(bg='#adffdd', width=40, anchor='w')
#     drop2["menu"].config(bg='#adffdd')
#     drop2.grid(row=0, column=1, columnspan=2)


# main-frame
frame = LabelFrame(root, padx=20, background='#e6ffe6', borderwidth=0, highlightthickness=0)
frame.pack(padx=5, pady=15)

# history frame
frame2 = LabelFrame(root, padx=20, background='#e6ffe6', borderwidth=0, highlightthickness=0)
frame2.pack(padx=5, pady=15, fill='both')

# headline text
headline_text = Label(frame, text="Path:", width=5, anchor=W, background='#e6ffe6')
headline_text.grid(row=0, column=0, sticky='w')

# entry field
entry = Entry(frame, width=65, borderwidth=2)
entry.grid(row=1, column=0, columnspan=1)

# okay button
okay_button = Button(frame, text="OK", command=lambda: okay_button_click(str(entry.get())), anchor='e', bg='#adffdd')
okay_button.grid(row=1, column=1, sticky='e', padx=10)

# Explore button
explore_button = Button(frame, text="Select Folder", command=explore, anchor='e', bg='#adffdd')
explore_button.grid(row=1, column=2, sticky='w')

# OR label
or_label = Label(frame2, text="OR", pady=10, bg='#e6ffe6')
or_label.grid(row=0, column=0, columnspan=3, sticky='ew')

# Select from these
select_from_these = Label(frame2, text="Select from these:", width=20, anchor=W, background='#e6ffe6', pady=25)
select_from_these.grid(row=1, column=0, sticky='w')

# drop down menu
history = read_write.read_files()
if len(history) == 0:
    read_write.write_to_file('/home/')
    history = read_write.read_files()
history.reverse()
clicked = StringVar()
clicked.set(history[0])
drop = OptionMenu(frame2, clicked, *history)
drop.config(bg='#adffdd', width=40, anchor='w')
drop["menu"].config(bg='#adffdd')
drop.grid(row=1, column=1, columnspan=1)

# second okay button
history_okay_button = Button(frame2, text="OK", command=lambda: okay_button_click(str(clicked.get())),
                             anchor='e', bg='#adffdd')
history_okay_button.grid(row=1, column=2, sticky='e', padx=10)

# root.filename = filedialog.askopenfilename(initialdir='~/Downloads', title='Select a file', filetypes=(("png
# files","*.png"), ("all files","*.*")))


root.mainloop()
