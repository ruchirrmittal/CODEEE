def rem_pr(str1,st2):
    if str1.startswith(st2):
        return str1[len(st2):]
    else:
        return str1

def rem_su(str1,st2):
    if str1.endswith(st2):
        return str1[:(len(str1)-len(st2))]
    else:
        return str1
    
n="my name is happy"
pre="my"
suf="happy"
result1=rem_pr(n,pre)
print(result1)
result2=rem_su(n,suf)
print(result2)