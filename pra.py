# for num in range(1,30):
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 break
#         else:
#          print(num) 


sum=0
for i in range(0,7,1):
    if not i%2==0:
        sum+=i

print(sum)
