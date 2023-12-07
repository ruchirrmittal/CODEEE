for num in range(1,30):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
         print(num) 


# sum=0
# for i in range(0,7,1):
#     if not i%2==0:
#         sum+=i

# print(sum)


# lis1=[]

# for i in range(3):
#     lis1.append([])
#     for j in range(1):
#         name=input("Name: \n")
#         lis1[i].append(name)
#         marks=int(input("Marks: \n"))
#         lis1[i].append(marks)

# print(lis1)        

# for i in range(len(lis1)):


# n = int(input())
# arr = map(int, input().split())
    
# a=sorted(arr)
    
# for i in range(n):
#     if a[(n-1)-i]==a[(n-2)-i]:
        
#         continue
#     else:
#         print(a[(n-2)-i])
#         break    

# str="my name is lobe"
# lis=str.split()
# print(lis)
# s="-".join(lis)
# print(s)

# # We need an empty dictionary, to store and display the letter frequencies.
# word_count = {}
 
# # Text string
# text = "Later in the course, you'll see how to use the collections Counter class."
 
# # Your code goes here ...
# for character in sorted(text.casefold()):
#     if character.isalnum():
#         print(character)
#         occ=0
#         word_count[character]=word_count.setdefault(occ,0)+1
#         print(word_count[character])
 
# # Printing the dictionary
# # for letter, count in word_count.items():
# #     print(letter, count)

# print(sorted(word_count))
# # We need an empty dictionary, to store and display the letter frequencies.
# word_count = {}
 
# # Text string
# text = "Later in the course, you'll see how to use the collections Counter class."
 
# # Iterate over every character in the string.
# for char in text.casefold():
#     # We're only counting letters and digits (no punctuation).
#     if char.isalnum():
#         word_count[char] = word_count.setdefault(char, 0) + 1
 
# # Printing the dictionary
# for letter, count in sorted(word_count.items()):
#     print(letter, count)


# 
# 
# 



# add(4,5)

# def pr(*a):
#     for i in a:
#         print(i)

# pr(1,2,3,4,5)