string=input("Enter the sentence:")
count=0  
for item in string:    
    count+=item.lower().count('a')  
print("No of times 'a' appears is:",count)      
        
