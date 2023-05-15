r=int(input("enter no. of rows =", ))
c=int(input("enter no. of coloums =", ))
ls=[]
print("enter first matrix element=")
for i in range(r):
    ls1=[]
    for j in range(c):
        y=int(input())
        ls1.append(y)
        
    ls.append(ls1)

print("entered matrix first =")
for i in range(r):
    for j in range(c):
        print(ls[i][j],end=" ")
    print()


ls2=[]
print("enter second matrix element=")
for i in range(r):
    ls3=[]
    for j in range(c):
        y=int(input())
        ls3.append(y)
        
    ls2.append(ls3)

print("entered matrix second =")
for i in range(r):
    for j in range(c):
        print(ls2[i][j],end=" ")
    print()

print("multiplication of two matrix =")

ls5=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(ls)):   
    for j in range(len(ls2[0])):
        for k in range(len(ls2)):
            ls5[i][j]+=ls[i][k]*ls2[k][j]
            
            


for i in range(r):
    for j in range(c):
        print(ls5[i][j],end=" ")
    print()
