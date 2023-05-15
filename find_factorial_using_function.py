def factorial(a):
    i=1
    f=1
    while(i<=a):
        f*=i
        i+=1
    print("factorial of a no. is:",f)
n=int(input("enter a number:"))
factorial(n)        