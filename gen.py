# import sys

# def my_range(n):
#     start = 0
#     for i in range(n):
#         yield start+i

# num=my_range(10)

# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print("this is generator")
# print(next(num))
# print(next(num))


# fibo

# def fib():
#     current,prev=0,1
    
#     while True:
#         current,prev=current + prev, current
#         yield current

# ser=fib()

# for i in range(10):
#     print(next(ser))