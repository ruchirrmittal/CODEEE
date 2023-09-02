# for num in range(1,30):
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 break
#         else:
#          print(num) 


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


n = int(input())
arr = map(int, input().split())
    
a=sorted(arr)
    
for i in range(n):
    if a[(n-1)-i]==a[(n-2)-i]:
        
        continue
    else:
        print(a[(n-2)-i])
        break    
