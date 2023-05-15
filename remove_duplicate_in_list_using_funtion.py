def duplicate(x):
    a=[]
    for i in x:
        if i not in a:
            a.append(i)
    return "".join(a)
ls=int(x for x in input().split())
str=duplicate(ls)
print("string after removing duplicate:",str)