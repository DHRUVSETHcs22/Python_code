def neon(x):
    m=x*x
    sum=0
    while(m!=0):
        a=m%10
        sum+=a
        m= m//10
    return sum
n=(int(input("enter a number:")))
p=neon(n)
if p==n:
    print("number is neon")
else:
    print("number is not neon")