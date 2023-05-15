def armstrong(x):
    p=0
    m=x
    while(m!=0):
        p+=1
        m=m//10
    sum=0
    while(x!=0):
        c=x%10
        sum=sum+pow(c,p)
        x=x//10
    return sum    
n=int(input("enter a number:"))
a=armstrong(n)
if a==n:
    print("number is armstonge")
else:
    print("number is not armstrong")    