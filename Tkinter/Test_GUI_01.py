# -*- coding: UTF-8 -*-

import Tkinter

def button_clicked(ev):
    n = int(ent1.get())
    win = Tkinter.Toplevel(root)
    win.focus_force()
    all_ent = []
    for i in xrange(n):
        ent = Tkinter.Entry(win, width=20, bd=3, font='arial 14')
        ent.grid(in_=win, row=i+1, column=1, pady=10)
    all_ent.append(ent)

    win.mainloop()

root = Tkinter.Tk()
btn = Tkinter.Button(root, text='Далее', width=5, height=2, bg='white', fg='black', font='arial 14')
ent1 = Tkinter.Entry(root, width=20, bd=3, font='arial 14')
ent1.focus_force()
ent1.pack()
btn.pack()
btn.bind('<Button-1>', button_clicked)
root.mainloop()
