list=int(input("Enter the no of integers to input:"))
integers=[]
for i in range(list):
    integer=int(input("Enter the no of integers:"))
    integers.append(integer)
    if(integer>100):
        integers[i]="over"
print(integers)
