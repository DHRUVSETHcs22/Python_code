def square(ls1):
    ls2=[]
    for i in ls1:
        ls2.append(i*i)
    print("after squaring list elements:",ls2)    
ls=(int(x) for x in input().split())    
square(ls)