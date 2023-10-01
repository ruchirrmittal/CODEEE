# file=open('Jabberwocky.txt',mode='r')

# for lines in file:
#     print(lines.lstrip())

# file.close()    

### Using With

# with open('Jabberwocky.txt','r') as f1:
#     for lines in f1:
#         print(lines.lstrip())

# with open('Jabberwocky.txt','r') as f1:
#     f2=f1.read()

# print(type(f2))

# for char in f2:
#     print(char,end="")

# with open('Jabberwocky.txt','r') as f1:
#     f2=f1.readlines()

# print(type(f2))

# for lines in f2:
#     print(lines.strip())

# with open('Jabberwocky.txt','r') as f1:
#     while True:
#         f2=f1.readline()
#         print(f2)

# -------------------------------------------

# #important


# with open('Jabberwocky.txt','r') as f1:
#     f2=f1.readline().rstrip()

# print(f2)    

# char="' Twasebv"
# f=f2.strip(char)
# print(f)


# --------------------------

# sen="My name is something and i am happy"

# rem_pre=sen.removeprefix("My")
# rem_suff=sen.removesuffix("happy")
# print(rem_pre)
# print(rem_suff)

# # 
# def rem_pr(str1,st2):
#     if str1.startswith(st2):
#         return str1[len(st2):]
#     else:
#         return str1

# def rem_su(str1,st2):
#     if str1.endswith(st2):
#         return str1[:(len(str1)-len(st2))]
#     else:
#         return str1
    
# n="my name is happy"
# pre="my"
# suf="happy"
# result1=rem_pr(n,pre)
# print(result1)
# result2=rem_su(n,suf)
# print(result2)

# ###############

# country file

file='country_info.txt'

with open(file) as f1:
    f1_c=f1.readline()

    for rows in f1:
        data=rows.strip('\n').split('|')
        print(data)

headers=f1_c.strip('\n').split('|')
print(headers)

       