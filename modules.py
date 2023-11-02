# import turtle
# import time

# turtle.forward(100)
# turtle.right(150)
# turtle.back(150)

# time.sleep(5)

# import turtle


# turtle.forward(100)
# # turtle.right(150)
# # turtle.back(150)

# turtle.done()

# avoid using- from turtle import.* as it may give error on identitical variables

# print(dir(__builtins__))

# import shelve

# for obj in dir(shelve.Shelf):
#     if obj[0]!='_':
#         print(obj)

# ----
# -----------
# -------------------


# import webbrowser

# webbrowser.open('https://www.youtube.com/watch?v=e-aaencD-dY')

# ---------------

# import time

# print(time.gmtime(0))

# print(time.localtime())

# time_here=time.localtime()

# print(f"Year:{time_here[0]}")
# print(f"Month:{time_here[1]}")
# print(f"Day:{time_here[2]}")

# ****************************
# Elapsed time

# import time
# from time import time as my_timer
# import random

# input("Press Enter to start")

# wait_time=random.randint(1,6)
# time.sleep(wait_time)
# start_time=my_timer()

# input("Press enter to stop")

# end_time=my_timer()

# print("Starting time is"+time.strftime("%X",time.localtime(start_time)))
# print("Ending time is"+time.strftime("%X",time.localtime(end_time)))

# print("the reaction difference is of {0} seconds".format(end_time-start_time))

# in the above code you can press enter twice to register in advance in order to cheat. therefore the code below is with the fixed code

# import time
# # from time import perf_counter as my_timer
# from time import monotonic as my_timer
# # from time import process_time as my_timer
# import random

# input("Press Enter to start")

# wait_time=random.randint(1,6)
# time.sleep(wait_time)
# start_time=my_timer()

# input("Press enter to stop")

# end_time=my_timer()

# print("Starting time is"+time.strftime("%X",time.localtime(start_time)))
# print("Ending time is"+time.strftime("%X",time.localtime(end_time)))

# print("the reaction difference is of {0} seconds".format(end_time-start_time))

# *****************************
# get_clock_info

# import time

# print("Time:{}".format(time.get_clock_info('time')))
# print("perf_time:{}".format(time.get_clock_info("perf_counter")))
# print("Time:{}".format(time.get_clock_info("monotonic")))
# print("Time:{}".format(time.get_clock_info("process_time")))

# *************************************************************************************


# import time

# print("The epoch of time is" + time.strftime('%c',time.gmtime(0)))

# print("the current timezone of {0} is {1}".format(time.tzname[0],time.timezone))

# if time.daylight!= 0:
#     print("Daylight saving is in effect")

# ________________________________________________________________________

# datetime

# import datetime

# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())

# ___________________________________________________________
# pytz module
# -------------------------------------------------------------

# import pytz
# import datetime

# country='Asia/Kolkata'

# tz_to_display=pytz.timezone(country)
# local_time=datetime.datetime.now(tz=tz_to_display)
# print("the time in {} is {}".format(country,local_time))

# ______________________________________________________________________________
# ______________________________________________________________________________
# ______________________________________________________________________________

# Functions2

# import tkinter

# def parabola(x):
#     y= x*x / 100
#     return y


# def draw_axes(canvas):
#     canvas.update()
#     x_origin=canvas.winfo_width() / 2
#     y_origin=canvas.winfo_height() / 2
#     canvas.configure(scrollregion=(-x_origin,-y_origin ,x_origin,y_origin))
#     canvas.create_line(-x_origin,0,x_origin,0,fill="black")
#     canvas.create_line(0,y_origin,0,-y_origin,fill="black")

# def plot_line(canvas,x,y):
#     canvas.create_line(x,y,x+1,y+1,fill="blue")

# mainwindow=tkinter.Tk()
# mainwindow.title("parabola")
# mainwindow.geometry("640x480")

# canvas=tkinter.Canvas(mainwindow,width=640,height=480)
# canvas.grid(row=0,column=0)

# draw_axes(canvas)

# for x in range(-100,100):
#     y=parabola(x)
#     plot_line(canvas,x,-y)


# mainwindow.mainloop()

import tkinter

def parabola(page,size):
    for x in range(-size,size):        
        y= x*x / size
        plot_line(page,x,y)


def draw_axes(page):
    page.update()
    x_origin=page.winfo_width() / 2
    y_origin=page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin,-y_origin ,x_origin,y_origin))
    page.create_line(-x_origin,0,x_origin,0,fill="black")
    page.create_line(0,y_origin,0,-y_origin,fill="black")

def plot_line(page,x,y):
    page.create_line(x,-y,x+1,-y+1,fill="blue")

mainwindow=tkinter.Tk()
mainwindow.title("parabola")
mainwindow.geometry("640x480")

canvas=tkinter.Canvas(mainwindow,width=640,height=480)
canvas.grid(row=0,column=0)

draw_axes(canvas)

parabola(canvas,100)
parabola(canvas,200)

mainwindow.mainloop()

