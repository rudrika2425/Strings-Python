s1=input()
s2=input()
s3=" "
for i in s1:
    if i not in s2:
        s3+=i
s2=s3        
print(s2)        
        