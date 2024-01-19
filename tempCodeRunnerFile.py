test=input("Enter something")

# output=[len(word) for word in test.split(" ")]
output=[(word,len(word)) for word in test.split(" ")]


print(output)