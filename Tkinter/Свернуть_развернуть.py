from tkinter import *
 
root = Tk()

label = Label(root, text='test').pack()
y = 0

def time_loop():
    global root
    global y

    if(y == 0):
        y = 1
        root.iconify()    
    else:
        y = 0
        root.deiconify()
   
    root.after(1000, time_loop)

time_loop() 
root.mainloop()