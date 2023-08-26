parts=["a","b","c","d","e"]

valid_choices=[]

for i in range(1,len(parts)+1):
    valid_choices.append(i)
print(valid_choices)   

choice="-"
listt=[]

while choice !=0:

    if choice in valid_choices:
        index=choice-1
        current=parts[index]

        if current in listt:
            print("Removing {}:{}".format(choice,parts[int(choice)-1]))
            listt.remove(current)
        else:
            print("Adding {}:{}".format(choice,parts[int(choice)-1]))
            listt.append(current)
        print(listt)        
    else:
        print("Please enter a valid option \n")
        for number,value in enumerate(parts):
            print("{}:{}".format(number+1,value))
    
    choice=int(input())        


print(listt)





