x=int(input("enter a number more than two dight:", ))
a=x
sum=0
while x!=0:
    r=x%10
    sum=sum*10+r
    x=x//10

if a==sum:
    print("given no. is palindrome")    

else:
    print("given no. is not palindrom")    