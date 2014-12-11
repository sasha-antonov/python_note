from Tkinter import *
import tkMessageBox as messagebox

def push_manual(event):
    win_1.destroy()
    win_2 = Tk()
    win_2.geometry('500x350')
    

def push_auto(event):
    win_1.destroy()
    win_2 = Tk()
    win_2.geometry('500x350')
    

win_1 = Tk()
win_1.geometry('290x135')

label_1 = Label(win_1, text='Choose:')
button_1 = Button(win_1, text='Manual')
button_2 = Button(win_1, text = 'Auto')

button_1.bind('<Button-1>', push_manual)
button_2.bind('<Button-1>', push_auto)

entry_1 = Entry(win_1, width=10)

label_1.place(x=10, y=10)
button_1.place(x=180, y=50)
button_2.place(x=10, y=50)
entry_1.place(x=180, y=90)
entry_1.insert(0, "COM1")
win_1.mainloop()
