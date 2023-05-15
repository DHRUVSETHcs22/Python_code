n=int(input("enter the number"))
ls=[]
for i in range(0,n):
    y=int(input())
    ls.append(y)
print("list before operation:",ls)
ls1=[]
for i in range(0,n):
    ls1.append(pow(ls[i],2))
print("list after operation:",ls1)    