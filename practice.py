# parts=["a","b","c","d","e"]

# valid_choices=[]

# for i in range(1,len(parts)+1):
#     valid_choices.append(i)
# print(valid_choices)   

# choice="-"
# listt=[]

# while choice !=0:

#     if choice in valid_choices:
#         index=choice-1
#         current=parts[index]

#         if current in listt:
#             print("Removing {}:{}".format(choice,parts[int(choice)-1]))
#             listt.remove(current)
#         else:
#             print("Adding {}:{}".format(choice,parts[int(choice)-1]))
#             listt.append(current)
#         print(listt)        
#     else:
#         print("Please enter a valid option \n")
#         for number,value in enumerate(parts):
#             print("{}:{}".format(number+1,value))
    
#     choice=int(input())        


# print(listt)

# odd=[1,3,5,7,9]
# even=[2,4,6,8,10]
# lis=[]

# for i in range(1,len(odd)+1):
#     # print(odd[i-1],end=" ")
#     lis.append(odd[i-1])
#     lis.append(even[i-1])

# print(lis)    

# alpha="aASSDAHUCIUEWHCEWfEGbcdefghikkdlsnwklxn"

# letter=sorted(alpha)
# print(letter)


# lis=['aa','bb','cc','dd','ee','ff','gg','hh']

# lis[2]='zz'

# print(lis)

# lis[2:4]="arara"

# print(lis)
# lis[2:4]=["arara"]
# print(lis)


# lis=[12,34,3,23,1324,5,3,12,21,314,4,22,12,4,54,223,2,3,658,769,45,3,4,3,33,5,767,4,3,5,77,6,74,2,2,100]
# print(len(lis))
# lis.sort()
# print(lis)

# stop=0

# for index,value in enumerate(lis):
#     if value>=20:
#         stop=index
#         break


# print(stop)
# del lis[:stop]
# print(lis)

# data=[1,3,6,22,55,3,10,6,6,33,6,10,444,24,5,3,22,555,33,22,66,77,88,99,100,111,122,434,22,22]

# # for index in range(len(data)-1,-1,-1):
# #     if data[index]<10 or data[index]>100:
# #         del data[index]

# # print(data)        

# # top_index=len(data)-1

# # for index,value in enumerate(reversed(data)):
# #     if value<10 or value>100:
# #         print(top_index-index,value)
# #         del data[top_index-index]

# # print(data)        

# # lists=[[1,2,3,44,6,3],[3,2,4,2,44,3]]

# # for numbers_l in lists:
# #     print(numbers_l,end="-------")
# #     for numbers in numbers_l:
# #         print(numbers,end=" ")
# menu = [
#     ["egg", "bacon"],
#     ["egg", "sausage", "bacon"],
#     ["egg", "spam"],
#     ["egg", "bacon", "spam"],
#     ["egg", "bacon", "sausage", "spam"],
#     ["spam", "bacon", "sausage", "spam"],
#     ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
#     ["spam", "egg", "spam", "spam", "bacon", "spam"],
# ]

# for meals in menu:
#     if "spam" in meals:
#         co=meals.count("spam")
#         if co>1:
#             for i in range(co):
#                 meals.remove("spam")
#             print("{} \n".format(meals))   
#             for items in meals:
#                 print(items,sep=", \n") 

#         else:
#             meals.remove("spam")
#             print("{} \n".format(meals)) 
#             for items in meals:
#                 print(items,end=",") 
#     else:
#         print("{} \n".format(meals))   
#         for items in meals:
#                 print(items,end=",")               

# list=['1','2','3','3','4']

# list1=",".join(list)
# print(list1)

# list2=list1.split(",")
# print(list2)

# for index in range(len(list2)):
#     list2[index]=

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),

    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),

    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
]


for name,artist,year,songs in albums:
    print(" Album : {} , Artist : {} , year {}".format(name,artist,year))
    for index,song in enumerate(songs):
        print("{}: {} ".format(index+1,song))