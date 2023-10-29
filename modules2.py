# import turtle

# def square(length):
#     for i in range(4):
#         turtle.forward(length)
#         turtle.right(90)


# for i in range(72):
#     square(50)
#     turtle.left(5)

# turtle.done()

# __________________________
# import turtle
# from math import radians,cos

# def square(length):
#     for i in range(4):
#         turtle.forward(length)
#         turtle.right(90)

# def encircled_sq(length):
#     square(length)
#     angle=radians(45)
#     radius=length*cos(angle)
#     turtle.right(135)
#     turtle.circle(radius)
    

# turtle.speed('fast')
# turtle.Screen().tracer(0)

# for i in range(72):
#     encircled_sq(50)
#     turtle.left(5)

# turtle.Screen().update()
# turtle.done()

# print(dir())


# read about local,global,builtin namespaces and scope

# LEGB the order python searches for name

# nested functions-vid468
# enclosing escope vid469
# a global variable cant be a free variable

# def myfunc():
#   x = 300
#   def myinnerfunc():
#     # nonlocal x
#     x=200
#     print(x)
  
#   myinnerfunc()
#   print(x)

# myfunc()

# another example for the global and nonlocal variable

# area=0

# def ar_sq(length):
#     global area
#     area=length*length

# ar_sq(30)
# print("The area of the square is {}".format(area))

# watch video 476 again

# if name=="__main__"
# watch the link
# https://www.youtube.com/watch?v=y_CX2Rvitk8

# _________________________________________________________________
# _________________________________________________________________

# note:
# strftime stands for string format time aka string from time
# strptime stands for string parse time aka time from string

# import datetime

# start=datetime.date(1999,2,24)
# print(start)

# word=start.strftime('%A %d %B %Y')

# print(word)

# year=start.year
# month=start.month

# print(f'the year is {year} and month is {month}')

# today=datetime.date.today()
# print(today)

# weekday=today.weekday()
# print(weekday)

# timedelta objects

# import datetime

# start=datetime.date(1999,2,24)
# print(start)

# word=start.strftime('%A %d %B %Y')

# print(word)

# duration=datetime.timedelta(days=2,weeks=1,hours=24)
# end=start+duration
# print(end)
# print(duration)

# datetime time module

# from datetime import date,time


# now=time(hour=1,minute=23,second=22)
# print(now)

# current=time()
# print(current)

# iso_format='11:23:23'
# timeiso=time.fromisoformat(iso_format)
# print(timeiso)

# 

# import datetime

# today1=datetime.date.today()
# today2=datetime.datetime.today()
# today3=datetime.datetime.now()
# utc1=datetime.datetime.utcnow()


# print(today1)
# print(today2)
# print(today3)
# print(utc1)
#

# __________________________________________
# ___________________________________________


# from datetime import datetime, timezone
# try:
#     import zoneinfo
# except ImportError:
#     from backports import zoneinfo

# utc_now = datetime.now(timezone.utc)
# print(utc_now)

# local_now = utc_now.astimezone()
# print(local_now)

# new_york_tz = zoneinfo.ZoneInfo('America/New_York')
# ny_now = utc_now.astimezone(tz=new_york_tz)
# print(ny_now)

# ______________________

from datetime import datetime, timezone
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

zones=(
    'Europe/Paris',
    'Europe/London',
    'Asia/Hong_Kong',
    'Africa/Nairobi'
)

utc_now=datetime.now(tz=timezone.utc)
utc_now=utc_now.replace(microsecond=0)

for zone in zones:
    tz=zoneinfo.ZoneInfo(zone)
    # required=datetime.now(tz=tz)
    required=utc_now.astimezone(tz)
    city=zone.split('/')[-1]
    print(f'The time in {city} is {required}')