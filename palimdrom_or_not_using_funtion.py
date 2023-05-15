def palindrom(x):
    rev=0
    while(x!=0):
        r=x%10
        rev=rev*10+r
        x=x//10
    return rev
n=int(input("enter a number:", ))
a=palindrom (n) 
if n==a:
    print("Yes given no. is palindrom") 
else:
    print("No given no. is not palindrom")    