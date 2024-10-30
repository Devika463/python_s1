str=input("Enter the string:")
print("The original string is:",str)
k='$'
new_str=str.replace(str[0],k).replace(k,str[0],1)
print("Replaced string:",new_str)
