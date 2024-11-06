string=input("Enter the string:")
for i in string:
    frequency=string.count(i)
    print(str(i)+":"+str(frequency),end=",")
