# def add(a,b):
    
#     result=a+b
#     return result


#  answer=add(3,4)
# print(answer)
# -----------------------------------------


# str="arraya"
# print(str[::-1])
# ------------------------------------------


# def is_pal(string):
#     return string.casefold()[::-1]==string.casefold()

# word=input("enter a string \n")
# ans=is_pal(word)

# if ans is True:
#     print("{} is a palindrom".format(word))
# else:
#     print("{} is not a palindrome".format(word))    
# --------------------------------------------------


# def is_pal(sen):
#     sen1=""

#     for char in sen:
#         if char.isalnum():
#             sen1+=char
    
#     print(sen1)        
#     return sen1.casefold()[::-1]==sen1.casefold() 


# sent=input("Enter a sen \n")
# ans=is_pal(sent)
# print(ans)
# if ans is True:
#     print("yes it is")
# else:
#     print("its not")    
# ------------------------------------


# def sum_eo(n,t):
    

#     if t.casefold()=='e':
#         sum=0
#         for i in range(0,n,2):
#             sum+=i
        
#         return sum
    
#     elif t.casefold()=='o':
#         sum=0
#         for i in range(0,n,1):
#             if not i%2==0:
#              sum+=i
#         return sum
     
#     else:
#         return -1

# num=int(input("Enter the number \n"))
# tt=input("Enter operation \n")
# ans=sum_eo(num,tt)
# print(ans)        
                        

# def sum_eo(n, t):
#     """Sum even or odd numbers in range.

#     Return the sum of even or odd natural numbers, in the range 1..n-1.

#     :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
#     :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
#     :return: The sum of the even or odd numbers in the range.
#             Returns -1 if `t` is not 'e' or 'o'.
#     """
#     if t == "e":
#         start = 2
#     elif t == 'o':
#         start = 1
#     else:
#         return -1

#     return sum(range(start, n, 2))


# x = sum_eo(10, 'e')
# print(x)


# --------------------------------------
# 

# a=7
# if a==7:
#     raise ValueError("a is seven")
# ---------------------------

# def multiply(x, y):
#     """
#     Multiply 2 numbers.
 
#     Although this function is intended to multiply 2 numbers,
#     you can also use it to multiply a sequence.  If you pass
#     a string, for example, as the first argument, you'll get
#     the string repeated `y` times as the returned value.
 
#     :param x: The first number to multiply.
#     :param y: The number to multiply `x` by.
#     :return: The product of `x` and `y`.
#     """
#     result = x * y
#     return result

# print(multiply.__doc__)
# ------------------------------------


# ***FIBONACCI***


# def fib(n):

#     if 0<=n<=1:
#         return n
    
#     n1,n2=1,0

#     result=None

#     for i in range(n-1):
#         result=n1+n2
#         n2=n1
#         n1=result

#     return result

# for i in range(20):
#     print(i,fib(i))
# ------------------------------------------------

# def add(a,b: int) ->bool:
    
#     result=a+b
#     return result


# answer=add()
# print(answer)

# sen=input(" \n")
# sen1=sen.split()
# print(sen1)

# for index in range(len(sen1)-1,-1,-1):
#     print(sen1[index],end=" ")

# def reverseString(input_str: str) -> str:
#     words = input_str.split()
#     reversed_str = " ".join(reversed(words))
#     return reversed_str

# # Example usage:
# original_str = input("Enter a string: ")
# reversed_result = reverseString(original_str)
# print("Reversed string:", reversed_result)

# str="cb we ewf w f we"
# a=str.split()
# print(a)
# aa=" ".join(a)
# print(aa)

# ------------------------------

# low=1
# high=1000

# print("please choose a number between 1 to 1000")
# input("press Enter to run")


# LOW=1
# HIGH=1000

# def guessbin(number,LOW,HIGH):
#     guesses=1

#     while True:
#         guess=LOW+(HIGH-LOW)//2
#         # hi_lo=input("my guess is {}. what to do next?".format(guess)).casefold()

#         # if hi_lo=="h":
#         if guess<number:
#             LOW=guess+1
#         # elif hi_lo=="l":
#         elif guess>number:
    
#             HIGH=guess-1
#         # elif hi_lo=="c":
#         elif guess==number:
#             return guesses
#             # print("winner in {}".format(guesses))
#             # break
#         # else:
#         #     print("enter something") 

    
#         guesses=guesses +1          
    
# for numbers in range(LOW,HIGH+1):
#     nog=guessbin(numbers,LOW,HIGH)
#     print("{} in {} guesses".format(numbers,nog))

# -----------------------------------------------------


# LOW=1
# HIGH=1000

# def guessbin(number,LOW,HIGH):
#     guesses=1

#     while True:
#         guess=LOW+(HIGH-LOW)//2
#         # hi_lo=input("my guess is {}. what to do next?".format(guess)).casefold()

#         # if hi_lo=="h":
#         if guess<number:
#             LOW=guess+1
#         # elif hi_lo=="l":
#         elif guess>number:
    
#             HIGH=guess-1
#         # elif hi_lo=="c":
#         elif guess==number:
#             return guesses
#             # print("winner in {}".format(guesses))
#             # break
#         # else:
#         #     print("enter something") 

    
#         guesses=guesses +1          


# corr=0
# maxc=0

# for numbers in range(LOW,HIGH+1):
#     nog=guessbin(numbers,LOW,HIGH)
#     print("{} in {} guesses".format(numbers,nog))

#     if nog>maxc:
#         maxc,corr=nog,1
#     elif nog==maxc:
#         corr+=1

# print("{} times {} guesses".format(corr,maxc))     
# ------------------------------------------------------------------------------

# import random

# def fizz_buzz(number):
#     if number%15==0:
#         return "fizz buzz"
#     elif number%3==0:
#         return "fizz"
#     elif number%5==0:
#         return "buzz"
#     else:
#         return str(number)
    

# # while True:
# #     ans=random.randint(1,100)
# #     res=fizz_buzz(ans)
# #     if res is False:
# #         print("lost")
# #         break
    
# #     ans=int(input("enter yours \n"))
# #     res=fizz_buzz(ans)
# #     if res is False:
# #         print(" you lost")
# #         break

# input("Press enter")
# print()

# next=0

# while next<99:
#     next+=1
#     print(fizz_buzz(next))
#     next+=1
#     correct_answer=fizz_buzz(next)
#     p1=input("Your move: \n")
#     if p1 != correct_answer:
#         print("{}".format(correct_answer))
#         break
# else:
#     print("well done {}".format(next))    

# ---------------------------

# def factorial(number:int) -> int:
#     """
#     """
#     if number==1 or number==0:
#         return 1
    

        
#     return number* factorial(number-1)  

# for n in range(6):
#     ans=factorial(n)
#     print("{} {}".format(n,ans))
    
# def factorial(n: int) -> int:
#     """Return n! (0! is 1)."""
#     if n <= 1:
#         return 1
 
#     result = 2
#     for x in range(3, n + 1):
#         result *= x
 
#     return result
 
 
# for i in range(6):
#     print(i, factorial(i))    
# ------------------------


# number=(1,4,2,4,2,3)

# print(number)
# print(*number)

# for i in number:
#     print(i)

# def a(arg):
#     print(arg)
#     print(*arg)

#     for i in arg:
#         print(i)

# a(number)
# a(1,4,2,4,2,3)
# a((1,4,2,4,2,3))


# def sum(*args):
#     result=0
#     print(*args)
#     for value in args:
#         result+=value
#     return result

# print(sum(1,2,3,4,5))        

