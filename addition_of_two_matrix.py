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

print("addition of 2 matrix =")

for i in range(r):
    for j in range(c):
        print(ls2[i][j] + ls[i][j],end=" ")  # for sutraction ls[i][j]-ls2[i][j]
    print()