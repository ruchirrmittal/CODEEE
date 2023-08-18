import random

guesses=1
highest=20

answer= random.randint(1,20)
print(answer)

print("Welcome to the guess game \n")

print("enter your number")
guess=int(input())

while guess !=answer:
    if guess>answer:
        print("go lower\n")
        guess=int(input())
    elif guess<answer:
        print("go higher")    
        guess=int(input())

    guesses= guesses+1    


print("win win in {}".format(guesses))