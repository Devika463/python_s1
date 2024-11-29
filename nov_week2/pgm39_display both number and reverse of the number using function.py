def rev_no(num):
    reverse=0
    while num>0:
        digit=num%10  
        reverse=reverse*10+digit  
        num=num//10 
    return reverse
def reverse_number():
    num=int(input("Enter a number with at least 4 digits: "))
    if num<1000:
        print("The number must have at least 4 digits!")
        return
    rev_num=rev_no(num)
    print("Original number:",num)
    print("Reversed number:",rev_num)
reverse_number()
