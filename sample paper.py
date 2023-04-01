b=input()
re=""
for i in b:
    if ord('a')<=ord(i)<=ord('z'):
        a=ord(i)-26-6
        re=re+chr(a)
    else:
        a=ord(i)+26+6
        re=re+chr(a)
print(re)               