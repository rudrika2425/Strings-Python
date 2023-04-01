s=input()
x=s.lower()
print(x)
re=""
for i in x:
    if i not in re:
        re+=i
if len(re)>1:
    print("diff")
else:
    print("same")
     
               