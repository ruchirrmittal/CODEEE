name =input("Enter your name \n")
age=int(input("Enter your age \n"))

if age>18 and age<31:
    print("Hey {0}!, your holiday is approved\n".format(name))
else:
    print("Hey {0}!, your holiday is not approved\n".format(name))
