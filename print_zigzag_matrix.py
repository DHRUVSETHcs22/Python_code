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

print("zigzag matrix =")
for i in range(0,r):
    if i%2==0:
        for j in range(0,c):
            print(ls[i][j],end=" ")
    else:
        for j in range(c-1,-1,-1):
            print(ls[i][j],end=" ")
    print()                
        