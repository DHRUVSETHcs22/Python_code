def even(x):
         if x%2==0:
           return True
         else:
           return False
ls=[1,2,4,5,7,9,8,6]
ls2=list(filter(even,ls))
print(ls2)
