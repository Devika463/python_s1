a=int(input("Enter the 4 digit number:"))
b=int(input("Enter the range:"))
c=[]
for i in range(1,1000):
     for j in range(a,b+1):
          if(i*i==j):
            if(j%2==0):
              c.append(j)
print("Even and Perfect Squares:")
print(c)
