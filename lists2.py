
"""
even=[2,4,6,8]
odd=[1,3,5,7,9]

numbers=[even,odd]

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)
        
        

"""
"""
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

        """


""""
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]



for meal in menu:
    if "spam" in meal:
        coun= meal.count("spam")
        if coun>1:
            for i in range(coun):
                meal.remove("spam")
            print(meal, end=" \n" )
            for value in meal:
                print(value, end=" ")    
        else: 
            meal.remove("spam")     
            print(meal, end=" \n") 
            for value in meal:
                print(value, end=" ")  

            

    else:
        print(meal, end=" \n")
        for value in meal:
            print(value,end=" ") 


"""""
"""""
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    for index in range(len(meal)-1,-1,-1):
        if meal[index]=="spam":
            del meal[index]

    print(meal)        """


