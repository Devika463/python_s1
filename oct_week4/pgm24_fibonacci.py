num=int(input("Enter the no:"))
n1=0
n2=1
n3=0
for i in range(0,num):
    print(n3,end=" ")
    n1=n2
    n2=n3
    n3=n1+n2
