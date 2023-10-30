import tkinter


prog=tkinter.Tk()

prog.title("this_is_something")
prog.geometry("360x360")

label1=tkinter.Label(prog,text="Enter your name")
label1.grid(row=1,column=1)

label2=tkinter.Label(prog,text=" ")
label2.grid(row=2,column=1)

name=tkinter.Entry(prog)
name.pack()

button1=tkinter.Button(prog,text="click me")
button1.grid(row=3,column=1)

prog.mainloop()