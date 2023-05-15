
import random
ls1=[]
for i in range(0,100):
    ls=[]
    for j in range(0,10):
        k=str(random.randint(0,9))
        if k in ls:
              continue
        else:
              ls.append(k)
    ls1.append(''.join(ls))
     
print("here are 100 lotery numbers:")
print(ls1)
print("first prize goes to %d lotery no."% random.randint(1,100))
print("second prize goes to %d lotery no."% random.randint(1,100))
