s=input("enter the string: ")
n=int(input("enter number of parts: "))
a=len(s)
while(n!=0):
    print(s[0:a//n])
    