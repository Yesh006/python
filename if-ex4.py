#logical operator

a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
c = int(input("Enter third number = "))
d = int(input("Enter fourth number = "))

if(a>b) and (a>c) and (a>d):
    print(a, "is big")
elif(b>c) and (b>d):
    print(b, "is big")
elif(c>d):
    print(c, "is big")
else:
    print(d, "is big")
