# av=["A",
#     "B",
#     "C",
#     "D",
#     "E",
#     "F"]

# options=[]
# for i in range(1,len(av)+1):
#     options.append(str(i))
# print(options)      

# choice="-"
# cart=[]

# while choice!= '0':
#     if choice in options:
        
        
#         index=int(choice)-1
#         current= av[index]
        
#         if current in cart:
#             print("removing {}".format(choice))
#             cart.remove(current)
#         else:    
#             print("Adding {}".format(choice))
#             cart.append(current)    

#         print("your cart contains {}".format(cart))    

#     else:
#         for number,part in enumerate(av):
#             print("{0}: {1} ".format(number +1,part))  

#     choice=input()


# print(cart)             
"""""
liss=[2,23,34,3,45,32,212,53,5,435,34,14,110,33,344,353,4523,34,4]
min=20
max=100

liss.sort()

stop=0

for index,value in enumerate(liss):
    if value >= min :
        stop=index
        break

print(stop)
del liss[:stop]
print(liss)  

start=0

for index in range(len(liss)-1,-1,-1):
    if liss[index]<=100:
        start=index + 1
        break

print(start)
del liss[start:]
print(liss)

"""""

# data = [44,3,555,33, 5, 104, 105, 110, 120, 130, 130, 150,
#             160, 170, 183, 185, 187, 188, 191, 350, 360]
# list_length = len(data)
     
# index = 0
# while index < list_length:
#     if data[index] <= 100 or data[index] >= 200:
#         del data[index]
#         index = index - 1
#         list_length -= 1
#     index += 1
# print(data)

lis1=[[(j*i) for j in range(4)] for i in range(4)]

print(lis1)
    

  