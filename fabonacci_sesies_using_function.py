def  fabonacci(x,a,b):
    for i in range(0,x):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

x=int(input("enter the range of series:"))
a=0
b=1
print(a,b,end=" ")
fabonacci(x,a,b)
