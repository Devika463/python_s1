n=int(input("Enter the no of elements:"))
numbers=[]
for i in range(n):
    x=int(input("Enter the no:"))
    numbers.append(x)
print(numbers)
while True:
    print("\n Menu")
    print("\n1Find the greatest and lowest no")
    print("\n2.Sort the list in ascending order")
    print("\n3.Create another list of even no")
    print("\n4.Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        print("Greatest no:",max(numbers))
        print("Lowest no:",min(numbers))
    elif choice=='2':
        print("Sorted list:",sorted(numbers))
    elif choice=='3':
        even_numbers=[]
        for num in numbers:
            if num%2==0:
                even_numbers.append(num)
        print("List of even numbers:",even_numbers)
    elif choice=='4':
        print("Exiting the program")
        break
    else:
        print("Invalid choice")
