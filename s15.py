s=input("enter the string: ")
re=" "
se=" "
for i in s:
    if i not in re:
        re+=i
    else:
        se+=i
    
print(se)            