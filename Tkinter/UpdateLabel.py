from tkinter import *
 
root = Tk()
 
var0=StringVar() 

label = Label(root, textvariable=var0).pack()
x = 'hello'

def time_loop():
    global x
    x = x + ' and you'
    var0.set(x)
    root.after(1000, time_loop)

time_loop() 
root.mainloop()
