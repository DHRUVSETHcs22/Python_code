def duplicate(x):
    x=list(x)
    a=[]
    for i in x:
        if i not in a:
            a.append(i)
    return "".join(a)
st=input("enter the string:", )
str=duplicate(st)
print("string after removing duplicate:",str)