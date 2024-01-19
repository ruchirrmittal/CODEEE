squares=[x**2 for x in range(1,10)]

print(squares)

# test=" a random set of words being put together"

# up=[word.upper() for word in test.split(" ")]

# print(up)

# numbers=input("Enter a series of numbers for square")

# squares=[int(num)**2 for num in numbers.split(" ")]
# print(squares) 

test=input("Enter something")

# output=[len(word) for word in test.split(" ")]
output=[(word,len(word)) for word in test.split(" ")]


print(output)