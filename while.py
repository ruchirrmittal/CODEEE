"""
exits=["n","w","s","e"]
chosen=""

while chosen not in exits:
    chosen=input("Please select exit\n")
    if chosen.casefold()=="quit":
        break 

if chosen.casefold()!="quit":
    print("you chose exit {}".format(chosen)) """

#for x in range(21):
 #   if x % 3 != 0 and x % 5 != 0:
  #      print(x)

for num in range(1,200):
    if num>1:
        for j in range(2,num):
            if (num%j)==0:
                break
            else:
                print(num)