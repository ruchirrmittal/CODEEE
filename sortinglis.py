"""""
x=["dwd","dwdg","qjijq","SJ","FCEO"]

x.sort(key=str.casefold())

print(x)

"""
"""""
lis=["aa","bb","cc","dd","ee","ff","gg"]

lis[2:4]=["rr"]
print(lis)

"""""
"""""
liss=[23,34,3,45,32,21,53,5,435,34,14,1,4]
del liss[1:5]
print(liss)
"""
"""""
liss=[2,23,34,3,45,32,21,53,5,435,34,14,1,4]
min=20
max=100

liss.sort()
stop=0

for index,value in enumerate(liss):
    if value >= min :
        stop=index
        break

print(stop)
del liss[:stop]
print(liss)    
"""""
"""""

data= [2,33,43,5,345,324,32,432,5,325,4,23,2,35,6,7,546,3,14343,7674,5,434,76,32,36,7,6]

top_index=len(data)-1

for index,value in enumerate(reversed(data)):
    if value>100 or value<10:
        print(top_index-index,value)
        del data[top_index-index]

print(data)        
"""""

