b=[]
size=int(input("Enter the size of array:"))
for i in range(size):
    clr=input("Enter the color:")
    b.append(clr)
print(b[0],b[-1],sep=",")
