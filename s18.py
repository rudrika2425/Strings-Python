s1=input("enter first string:")
s2=input("enter first string:")
n1=len(s1)
n2=len(s2)
flag=0
if(n1>=n2):
    for i in s2:
        if i not in s1:
            flag=1
            break
        
            
if flag==1:
    print("not an annagram")
else:
    print("anagram")            