x=int(input("enter a three dight number:"))
y=x

a=x%10
a=a**3

x=x//10

b=x%10
b=b**3

c=x//10
c=c**3

z=a+b+c

if z==y:
    print("no. is armstrong")

else :
    print("no. is not armstron")
        


