#nested if control
a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
c = int(input("Enter third number = "))

if(a>b):
    if(a>c):
        print(a,"is big")
    else:
        print(c,"is big")
elif(b>c):
    print(b,"is big")
else:
    print(c,"is big")
