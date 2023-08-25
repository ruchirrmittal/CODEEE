ans=55

guess=int(input())
guesses=1

while guess!=ans:
    if guess>ans:
        print("lower")
        guess=int(input())
    else:
        print("higher")
        guess=int(input())

    guesses=1+guesses    
else:
    print("correct {}".format(guesses))    

print("sss")           