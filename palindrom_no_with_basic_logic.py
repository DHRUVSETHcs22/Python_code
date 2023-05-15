x=int(input("enter a three dight number:", ))
z=x
a=x%10

x=x//10

b=x%10

c=x//10

y=a*100+b*10+c

if y==z:
    print("no. is palindrome")

else:
    print("no. is not palindrome")   

