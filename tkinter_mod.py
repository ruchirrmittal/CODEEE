# import tkinter

# # print(tkinter.TkVersion)
# # print(tkinter.TclVersion)

# # tkinter._test()

# mainwindow=tkinter.Tk()

# mainwindow.title("hello world")
# mainwindow.geometry('640x360')

# e=tkinter.Entry(mainwindow)
# e.pack()



# label=tkinter.Label(mainwindow,text='My name is Ruchir')
# label.pack(side='top')

# # canvas=tkinter.Canvas(mainwindow,relief='raised',borderwidth=10)
# # canvas.pack(side='left')
# # canvas.pack(side='top',fill=tkinter.BOTH,expand=True)
# # canvas.pack(side='top',fill=tkinter.Y,expand=True)
# # canvas.pack(side='top',fill=tkinter.X,expand=True)
# def click():
#     label1=tkinter.Label(mainwindow,text= "thanks for clicking me")
#     label1.pack(side='bottom')


# button1=tkinter.Button(mainwindow,text="button1",command=click)
# button2=tkinter.Button(mainwindow,text="button2")
# button3=tkinter.Button(mainwindow,text="button3")
# button1.pack(side='bottom')
# button2.pack(side='left')
# button3.pack(side='top')



# mainwindow.mainloop()

# _______________________________

# root=tkinter.Tk()

# root.title("test1")
# root.geometry('360x360')

# label1=tkinter.Label(root,text="My name is")
# label2=tkinter.Label(root,text="Ruchir Mittal")

# label1.grid(row=0,column=0)
# label2.grid(row=1,column=1000)

# root.mainloop()
# _______________


# import tkinter


# prog=tkinter.Tk()

# prog.title("this_is_something")
# prog.geometry("360x360")

# label1=tkinter.Label(prog,text="Enter your name")
# label1.pack()

# label2=tkinter.Label(prog,text=" ")
# label2.pack()

# name=tkinter.Entry(prog)
# name.pack()
# name.insert(0,"Enter your name:")

# def nameg():
#     label3=tkinter.Label(prog,text=f'my name is {name.get()}')
#     label3.pack()

# button1=tkinter.Button(prog,text="click me",command=nameg)
# button1.pack()

# def clear():
#     name.delete(0,)
    

# button2=tkinter.Button(prog,text="clear",command=clear)
# button2.pack()

# prog.mainloop()

# # _______________________________________----

# import tkinter
# from PIL import ImageTk,Image

# prog1=tkinter.Tk()

# prog1.title("tkinterlesson")
# prog1.geometry("640x640")
# prog1.iconbitmap("C:/Users/Hewlett-Packard/Downloads/lala.ico")

# my_img=ImageTk.PhotoImage(Image.open("C:/Users/Hewlett-Packard/Downloads/lala1.jpg"))
# labelimg=tkinter.Label(image=my_img)
# labelimg.pack()


# die_button=tkinter.Button(prog1,text="Click me to die",command=prog1.quit)
# die_button.pack()

# _________________________
# image viewer
# __________________________

# import tkinter
# from PIL import ImageTk,Image

# viewer=tkinter.Tk()

# viewer.title("tkinterlesson")
# viewer.geometry("640x640")
# viewer.iconbitmap("C:/Users/Hewlett-Packard/Downloads/lala.ico")

# my_img=ImageTk.PhotoImage(Image.open("C:/Users/Hewlett-Packard/Downloads/lala1.jpg"))
# my_img1=ImageTk.PhotoImage(Image.open("C:/Users/Hewlett-Packard/Downloads/lala2.jpg"))
# my_img2=ImageTk.PhotoImage(Image.open("C:/Users/Hewlett-Packard/Downloads/lala3.jpg"))
# my_img3=ImageTk.PhotoImage(Image.open("C:/Users/Hewlett-Packard/Downloads/lala4.jpg"))

# image_list=[my_img,my_img1,my_img2,my_img3]

# labelimg=tkinter.Label(image=my_img)
# labelimg.grid(row=1,column=0,columnspan=3)


# die_button=tkinter.Button(viewer,text="Click me to die",command=viewer.quit)
# die_button.grid(row=0,column=1)

# back=tkinter.Button(viewer,text="<<<<")
# back.grid(row=0,column=0)

# forward=tkinter.Button(viewer,text=">>>>")
# forward.grid(row=0,column=2)

# viewer.mainloop()
