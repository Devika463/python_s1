list1=input("Enter the 1st list separated by spaces:").split()
list2=input("Enter the 2nd list separated by spaces:").split()
for i in range(len(list1)):
    list1[i]=int(list1[i])
for i in range(len(list2)):
    list2[i]=int(list2[i])
if (len(list1)==len(list2)):
    print("List are of same length")
else:
    print("List are of different length")
if (sum(list1)==sum(list2)):
     print("List sum to same value")
else:
    print("List sum to different value")
common_values=set(list1)&set(list2)
if common_values:
    print("Common_values:",common_values)
else:
    print(" No Common_values")
