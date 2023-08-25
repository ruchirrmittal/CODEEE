#result="abcd"

#an_result=result
#print(id(result))
#print(id(an_result))

#result += "efg"
#an_result=result
#print(id(result))
#print(id(an_result))
"""
result = 55
another_result = result
print(id(result))
print(id(another_result))

print()
result += 55
print(id(result))
print(id(another_result))
     
print()
another_result = result
print(id(another_result))

"""
"""""
h="my name is alice"

count=0


for i in h:
    if i=="a":
        count +=1


print(count)     
"""   
""""
choice="-"
computer_parts = []

while choice != '0' :

    if choice in "123456":
        print(" Adding {}".format(choice) )
        if choice=='1':
            computer_parts.append("A")
        elif choice=='2':
            computer_parts.append("B")
        elif choice=='3':
            computer_parts.append("C")
        elif choice=='4':
            computer_parts.append("D")
        elif choice=='5':
            computer_parts.append("E")
        elif choice=='6':
            computer_parts.append("F")            

    else:
        print("Please select an option from below \n")
        print("1: A")
        print("2: B")
        print("3: C")
        print("4: D")
        print("5: E")
        print("6: F")
        print("0: EXIT")

    choice=input()


print(computer_parts)
        

"""

""""
available_parts=["a","b","c","d","e"]

for part in available_parts:
    print("{0}: {1}".format(available_parts.index(part)+1,part))

""" 
#using enumerate to replace the loop above

# available_parts=["a","b","c","d","e"]

#for number,part in enumerate(available_parts):
#    print("{0}: {1}".format(number+1,part))

#value_choices= [str(i) for i in range(1,len(available_parts)+1)]
"""""
value_choices=[]
for i in range(1,len(available_parts)+1):
    value_choices.append(i)
print(value_choices)

"""
"""""

available_parts = ["a","b","c","d","e","f"]

valid_choices=[]
for i in range(1,len(available_parts)+1):
    valid_choices.append(str(i))
print(valid_choices)

choice="-"
computer_parts=[]

while choice != '0' :

    if choice in valid_choices:
        print(" Adding {}".format(choice) )

        index=int(choice)-1
        current=available_parts[index]
        computer_parts.append(current)            

    else:
        for part in available_parts:
            print("{0}: {1}".format(available_parts.index(part)+1,part))


    choice=input()


print(computer_parts)

"""""