r=int(input("enter no. of rows =", ))
c=int(input("enter no. of coloums =", ))
ls=[]
print("enter matrix element=")
for i in range(r):
    ls1=[]
    for j in range(c):
        y=int(input())
        ls1.append(y)
        
    ls.append(ls1)
    
print("entered matrix =")
for i in range(r):
    for j in range(c):
        print(ls[i][j],end=" ")
    print() 

print("transpose of matrix =")
for i in range(0,r):
    for j in range(0,c):
        print(ls[j][i])    
    print()    