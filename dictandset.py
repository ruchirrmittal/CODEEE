# vehicles = {
#     'dream': 'Honda 250T',
#     'roadster': 'BMW R1100',
#     'er5': 'Kawasaki ER5',
#     'can-am': 'Bombardier Can-Am 250',
#     'virago': 'Yamaha XV250',
#     'tenere': 'Yamaha XT650',
#     'jimny': 'Suzuki Jimny 1.5',
#     'fiesta': 'Ford Fiesta Ghia 1.4',
# }


# #printing specific values in a dict
# a=vehicles['er5']
# b=vehicles.get('jimny')
# print(a)
# print(b)


# iteration
# for key in vehicles:
#     a=vehicles[key]
#     print(a)


# iteration using dot items
# for key,value in vehicles.items():
#     print(key,value,sep=" : ")


# adding value to dict
# vehicles['soso']="ooga booga boo" 
# for key,value in vehicles.items():
#     print(key,value,sep=" : ")



# adding values over iteration
# for i in range(3):
#     key=input("key \n")
#     value=input("value \n")
#     vehicles[key]=value

# for key,value in vehicles.items():
#     print(key,value,sep=" : ")


# changing values 
# vehicles = {
#     'dream': 'Honda 250T',
#     'roadster': 'BMW R1100',
#     'er5': 'Kawasaki ER5',
#     'can-am': 'Bombardier Can-Am 250',
#     'virago': 'Yamaha XV250',
#     'tenere': 'Yamaha XT650',
#     'jimny': 'Suzuki Jimny 1.5',
#     'fiesta': 'Ford Fiesta Ghia 1.4',
# }


# vehicles['dream']="ice cream"
# for key in vehicles:
#     print(key,vehicles[key],sep=" : ")


# removing values

# del vehicles["dream"]

# vehicles.pop("jimny",None)
# vehicles.pop("huaha",None)

# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------


# available_parts = {'1': "computer",
#                         '2': "monitor",
#                         '3': "keyboard",
#                         '4': "mouse",
#                         '5': "hdmi cable",
#                         '6': "dvd drive",
#                     }

# choice="-"
# while choice !='0':
#     if choice in available_parts:
#         a=available_parts[choice]
#         print(f"adding {a}\n")
#     else:
#         for key,values in available_parts.items():
#             print(f"{key}:{values}")

#     choice=input(">")           

# choice="-"
# cart={}
# while choice !='0':
#     if choice in available_parts:
#         a=available_parts[choice]
#         print(f"adding {a}\n")
#         cart[choice]=available_parts[choice]
#         print(cart)
#     else:
#         for key,values in available_parts.items():
#             print(f"{key}:{values}")

#     choice=input(">")           


# -------------------------------------------------------------

# --------------------------------------------------------------
############# SMART FRIDGE ########################


# from contents import pantry , recipes


# display={}

# def adder(list,fo_it,q):
#     # list[fo_it]=q
#     # return listt
#     # if fo_it in list:
#     #     list[fo_it]+=q
#     # else:
#     #     list[fo_it]=q   

#     list[fo_it]=list.setdefault(fo_it,0) + q 


# for index,value in enumerate(recipes):
#     display[str(index+1)]=value

# shopping_list={}

# while True:
    
#     print("Please choose a recipe:")
#     print("-"*10)

#     for key,value in display.items():
#         print(f"{key}: {value}")

#     choice=input("-:")  
#     if choice=='0':
#         break
#     elif choice in display:
#         selected=display[choice]
#         print(f"You have selected {selected}")
#         print()
#         print("checking ingredients....")
#         ingredients=recipes[selected]
#         for key in ingredients:
#             # r1=ingredients[key]
#             print(f"{key}") 
#         for food,qua in ingredients.items():
#             qua_p=pantry.get(food,0)
#             if qua<=qua_p:
#                 print(f"{food} ok")
#             else:
#                 quantitytobuy=qua-qua_p
#                 print(f"{food} is not enough,get {quantitytobuy} more")
#                 adder(shopping_list,food,quantitytobuy)

# print(shopping_list)        

# ---------------------------------------------
# Dict methods
#------------------------------------------------
# d = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine",
# }

# pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon'] 

# new_dict=dict.fromkeys(pantry_items,0) 
# #Create a new dictionary with keys from iterable and values set to value
# print(new_dict)

# keyss=d.keys()
# print(keyss)

# v=d.values()
# print(v) 
# values=list(v)
# print(values)

# animals={'a':['cool','fun','awesome'],
#          'b':['bad','bob','bongus'],
#          'c':['cute','curly','cunt'],

# }

# print(animals['c'])
# words=animals.copy()
# print(words['c'])

# words['c'].append("coco")

# print(animals['c'])
# print(words['c'])

# dic1={'1':['one','two','three'],
#       '2':['ek','do','teen',]}

# dic2={}

# key=dic1.keys()
# print(key)
# value=dic1.values()
# print(value)

# data=[('da','a'),
#       ['aba','sns']]

# print(ord("a"))

# def sh(str):
#     basic_hash=ord(str[0])
#     return basic_hash%10

# print(sh('a'))
# -------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------



# SETS

import random

a=random.randrange(2,10,2)
print(a)