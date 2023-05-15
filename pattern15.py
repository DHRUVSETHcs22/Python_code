r=int(input("enter the no. of rows=",))
m=4
n=5
for i in range(0,r):
    for z in range(r,1,-1):
        print(" "*m,end=" ")
    for j in range(0,r):
        if(i==0  or j==0 ):
            print(" *",end=" ")   
        else:
            print('  ',end=" ")    
       
    print()
    m-=1 
    
    for i in range(0,r):
      for z in range(r,1,-1):
        print(" "*n,end=" ")
      for j in range(0,r):
        if( j==r-1 ):
            print(" *",end=" ")   
        else:
            print('  ',end=" ")    
       
      print()
      n+=1   
      break    
                                      


n=1
m=12
for i in range(0,r):
    for z in range(r,1,-1):
        print(" "*n,end=" ")
    for j in range(0,r):
        if( i==r-1 or j==0 ):
            print(" *",end=" ") 
              
        else:
            print('  ',end=" ")    
       
    print()
    n+=1
    

    for i in range(0,r):
      for z in range(r,1,-1):
        print(" "*m,end=" ")
      for j in range(0,r+1):
        if(j==0):
           print(" *",end=" ") 
           break
        else:
            print('  ',end=" ")    
       
      print()
      m-=1      
      break

 