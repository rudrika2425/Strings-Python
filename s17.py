s=input("enter the string: ")
for i in s:
    if i=="b":
        s=s.replace(i," ")
    if "ac" in s:
        s=s.replace("ac"," " )
print(s)        