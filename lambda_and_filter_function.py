ls1=[1,2,3,5,7,8,9,10]
ls2=[1,2,4,8,9]
ls=list(filter(lambda x:x in ls1, ls2))
print(ls)
