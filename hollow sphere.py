r=int(input("enter the no. of rows=",))
for i in range(0,r):
    for j in range(0,r):
        if(i==0 or i==r-1 or j==0 or j==r-1):
            print("*",end=" ")   
        else:
            print(' ',end=" ")    
       
    print()                    