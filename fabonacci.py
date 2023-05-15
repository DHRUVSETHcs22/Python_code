x=0
y=1
c=int(input("enter the range of series:", ))
print(x,y,end=" ")

i=1
temp=0
while(i<=c):
    z=x+y
    print(z,end=" ")
    temp=x
    x=y
    y=z
    i+=1

    

