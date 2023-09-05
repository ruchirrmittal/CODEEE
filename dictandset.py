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
vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}


# vehicles['dream']="ice cream"
# for key in vehicles:
#     print(key,vehicles[key],sep=" : ")


# removing values

# del vehicles["dream"]

# vehicles.pop("jimny",None)
# vehicles.pop("huaha",None)

# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------


available_parts = {'1': "computer",
                        '2': "monitor",
                        '3': "keyboard",
                        '4': "mouse",
                        '5': "hdmi cable",
                        '6': "dvd drive",
                    }

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


from contents import pantry , recipes


display={}

for index,value in enumerate(recipes):
    display[str(index+1)]=value

while True:
    print("Please choose a recipe:")
    print("-"*10)

    for key,value in display.items():
        print(f"{key}: {value}")

    choice=input("-:")  
    if choice=='0':
        break
    elif choice in display:
        selected=display[choice]
        print(f"You have selected {selected}")
        print()
        print("checking ingredients....")
        ingredients=recipes[selected]
        for key in ingredients:
            value=ingredients[key]
            print(f"{value}") 
        for food,qua in ingredients.items():
            qua_p=pantry.get(food,0)
            if qua<=qua_p:
                print(f"{food} ok")
            else:
                quantitytobuy=qua-qua_p
                print(f"{food} is not enough,get {quantitytobuy} more")    
                


        


      