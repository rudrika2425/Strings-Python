s=input()
n=len(s)
a=b=c=0
for i in range(n):
    if (s[i]=="a"or s[i]=="e"or s[i]=="i" or s[i]=="o"or s[i]=="u"):
        a+=1
    if (s[i]==" "):
        b+=1
    else:
        c+=1    
print("vowels=",a,"white spaces=",b,"consonants=",c)        