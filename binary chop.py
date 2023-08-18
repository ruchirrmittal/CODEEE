low=1
high=10000

print("please choose a number between 1 to 1000")
input("press Enter to run")

guesses=1

while low!=high:
    guess=low+(high-low)//2
    hi_lo=input("my guess is {}. what to do next?".format(guess)).casefold()

    if hi_lo=="h":
        low=guess+1
    elif hi_lo=="l":
        high=guess-1
    elif hi_lo=="c":
        print("winner in {}".format(guesses))
        break
    else:
        print("enter something") 

    
    guesses=guesses +1          
else:
    print("win win")