x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))
if(x>y and x>z):
    print("Largest number is",x)
elif(y>x and y>z):
    print("Largest number is",y)
else:
    print("Largest number is",z)
