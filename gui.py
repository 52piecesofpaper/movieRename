from tkinter import *
from tkinter import filedialog

import PIL
from PIL import Image
from PIL import ImageTk

import test

# root initialisation
root = Tk()
root.title('Organise Your Movies')
# root.geometry("800x600")
root.resizable(False, False)
root.configure(background='#e6ffe6')
img = ImageTk.PhotoImage(PIL.Image.open("/home/pratik/PycharmProjects/renameGUI/icons8.png"))
root.iconphoto(True, img)


# Functions
def okay_button_click():
    test.write_to_file(entry.get())
    entry.delete(0, 'end')


def choose_directory():
    dir_name = filedialog.askdirectory()
    test.write_to_file(str(dir_name))


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
entry = Entry(frame, width=70, borderwidth=2)
entry.grid(row=1, column=0, columnspan=1)

# okay button
okay_button = Button(frame, text="OK", command=okay_button_click, anchor='e', bg='#adffdd')
okay_button.grid(row=1, column=1, sticky='e', padx=2)

# Explore button
explore_button = Button(frame, text="Select Folder", command=choose_directory, anchor='e', bg='#adffdd')
explore_button.grid(row=1, column=2, sticky='w')

# separator
# separator = tkinter.ttk.Separator(frame2, orient=HORIZONTAL).grid(row=0, column=0, columnspan=3, sticky='we')

# Or select from these
select_from_these = Label(frame2, text="Or select from these:", width=20, anchor=W, background='#e6ffe6')
select_from_these.grid(row=0, column=0, sticky='w')

# drop down menu
history = test.read_files()
history.reverse()
clicked = StringVar()
clicked.set(history[0])
drop = OptionMenu(frame2, clicked, *history)
drop.config(bg='#adffdd')
drop["menu"].config(bg='#adffdd')
drop.grid(row=0, column=1)


# root.filename = filedialog.askopenfilename(initialdir='~/Downloads', title='Select a file', filetypes=(("png
# files","*.png"), ("all files","*.*")))


root.mainloop()
