n=["a","b","c","d"]
print("My list before swapping:",n)
length=len(n)
temp=n[0]
n[0]=n[length-1]
n[length-1]=temp
print("After swapping my list:",n)
