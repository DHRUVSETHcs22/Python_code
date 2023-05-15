a=int(input('enter the first no.', ))
b=int(input('enter the second no.', ))
y=(lambda x,y : x if x>y else y)
print('gretest no. ',y(a,b))
