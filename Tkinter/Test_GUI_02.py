from Tkinter import *

class But_print:
    def __init__(self):
        self.but = Button(root)
        self.but['text'] = 'Print'
        self.but.bind('<Button-1>', self.printer)
        self.but.pack()
    def printer(self, event):
        self.x = 'Hello World'
        print(self.x)
        self.name_group = obj_4.ent.get()
        print(self.name_group)

class Label_my:
    def __init__(self):
        self.lab = Label(root, text="Input name for you team")
        self.lab.pack()

class Entry_my:
    def __init__(self):
        self.ent = Entry(root, width=20, bd=3)
        self.ent.pack()

class Text_my:
    def __init__(self):
        self.tex = Text(root, width=30)
        self.tex.pack()

class Radiobutton_my:
    def __init__(self):
        self.var = IntVar()
        self.var.set(1)
        self.rad0 = Radiobutton(root, text = 'one', variable = self.var, value = 0)
        self.rad1 = Radiobutton(root, text = 'two', variable = self.var, value = 1)
        self.rad2 = Radiobutton(root, text = 'one', variable = self.var, value = 3)
        self.rad0.pack()
        self.rad1.pack()
        self.rad2.pack()

class Checkbutton_my:
    def __init__(self):
        self.c1 = IntVar()
        self.c2 = IntVar()
        self.check_1 = Checkbutton(root, text = 'one flag', variable = self.c1,
                                   onvalue = 1, offvalue=0)
        self.check_2 = Checkbutton(root, text = 'two flag', variable = self.c2,
                                   onvalue = 1, offvalue = 0)
        self.check_1.pack()
        self.check_2.pack()

class Listbox_my:
    def __init__(self):
        self.list_my = Listbox(root, selectmode=SINGLE, height=3)
        self.list_my.insert(END, "One")
        self.list_my.insert(END, "Two")
        self.list_my.insert(END, "Three")
        self.list_my.pack()

class Menu_my:
    def __init__(self):
        self.menu_my = Menu(root)
        root.config(menu=self.menu_my)

        self.fm = Menu(self.menu_my)
        self.menu_my.add_cascade(label="File", menu=self.fm)
        self.fm.add_command(label="Open", command=self.print_hello)
        self.fm.add_command(label="New", command=self.print_hello)

        self.hm = Menu(self.menu_my)
        self.menu_my.add_cascade(label='Help', menu=self.hm)
        self.hm.add_command(label='Help')
        self.hm.add_command(label='About')

        self.nfm = Menu(self.fm)
        self.fm.add_cascade(label='Import', menu=self.nfm)
        self.nfm.add_command(label='Image')
        self.nfm.add_command(label='Text')

    def print_hello(self):
        print('Hello World')
        

root = Tk()
obj_1 = But_print()
obj_2 = But_print()
obj_3 = Label_my()
obj_4 = Entry_my()
obj_5 = Text_my()
obj_6 = Radiobutton_my()
obj_7 = Checkbutton_my()
obj_8 = Listbox_my()
obj_9 = Menu_my()
root.mainloop()
