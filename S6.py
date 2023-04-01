s=input("enter the string: ")
re=""
for i in s:
    if (ord(i)>=65 and ord(i)<=90)or(ord(i)>=97 and ord(i)<=122):
        re+=i
print(re)        
        
        