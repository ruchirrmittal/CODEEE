# import sys

# def my_range(n):
#     start = 0
#     for i in range(n):
#         yield start+i

# num=my_range(10)

# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print("this is generator")
# print(next(num))
# print(next(num))


# fibo

# def fib():
#     current,prev=0,1
    
#     while True:
#         current,prev=current + prev, current
#         yield current

# ser=fib()

# for i in range(10):
#     print(next(ser))

# odd number generator

# def odd():
#     n=1
#     while True:
#         yield n
#         n+=2

# series=odd()
# # print(series)
# # print(next(series))

# for i in range(100):
#     print(next(series))

# the os walk generator

import os

root="music"

# for path,dirs,files in os.walk(root,topdown=True):
#     print(path)
#     for f in files:
#         print(f)

# ------------------------------------


# for path,dirs,files in os.walk(root,topdown=True):
#     if files:
#         print(path)
#         head_tail=os.path.split(path)
#         print(head_tail)
#         head=os.path.split(head_tail[0])
#         print(head)
#         for f in files:
#             song=f[:-5].split(" - ")
#             print(song[1])
#         input()

# ----------------------------------
# import fnmatch

# def findalbum(root,artist):
#     for path,dirs,file in os.walk(root):
#         for artist in fnmatch.filter(dirs,artist):
#             subdir=os.path.join(path,artist)
#             for album_path,albums,_ in os.walk(subdir):
#                 for album in albums:
#                     yield os.path.join(album_path,album),album

# # find=findalbum(root,"Aerosmith")

# # print(next(find))
# # print(next(find))
# # print(next(find))
# # print(next(find))
# # print(next(find))




