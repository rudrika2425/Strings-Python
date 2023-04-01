s=input("enter the string: ").split()
l=list(s)
re=[]
for i in l:
    if i not in re:
        re.append(i)
    else:
        l.remove(i)    
print(re)
print(l)        