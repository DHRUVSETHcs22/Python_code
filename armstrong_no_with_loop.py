x=int(input("enter a number more than two dight:", ))
z=1

y=x
c=0
while (y!=0):
    y//=10
    c+=1

a=x
sum=0
while x!=0:
    r=x%10
    sum=sum+r**c
    x=x//10

if a==sum:
    print("given no. is armstrong")    

else:
    print("given no. is not armstrong")    