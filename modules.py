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

import time

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

