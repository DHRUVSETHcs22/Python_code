def perfect():
    n=int(input("enter the number:", ))
    m=n
    sum=0
    i=1
    while(i<m):
        if(m%i==0):
            sum+=i
        i+=1
    if sum == n:
        print("no. is perfect")
    else:
        print("no. is not perfect")            

perfect()        