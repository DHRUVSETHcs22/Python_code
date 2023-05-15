x=int(input("enter a number more than two dight:", ))
sum=0
while x!=0:
    r=x%10
    sum=sum*10+r
    x=x//10

print("reverse no:", +sum)