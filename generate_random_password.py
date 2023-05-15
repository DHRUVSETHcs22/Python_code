import random
ls="0123456789"
st1="aqwsxzcderfvbgtyhnmjuiklop"
st2="AWQZSEXCDRFVBGTYHNMJUIKLOP"
st="!@#$&*"
a=random.choice(ls)
b=random.choice(st)
c=random.choice(st1)
d=random.choice(st2)
e=a+b+c+d
e=list(e)
random.shuffle(e)
print( ' '.join(e))