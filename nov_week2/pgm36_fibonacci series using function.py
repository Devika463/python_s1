def fibo(n):
   if n<=1:
       return n
   else:
       return(fibo(n-1)+fibo(n-2))
num=int(input("Enter the no:"))
if num<= 0:
   print("Enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(num):
       print(fibo(i))
