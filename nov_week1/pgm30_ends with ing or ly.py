string=input("Enter the string:")
if string.endswith('ing'):
    string+='ly'
else:
    string+='ing'
print(string)
