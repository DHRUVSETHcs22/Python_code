                              #Anonymous Functions or Lambdas or function without a name
# a lambda function to calculate square value
f=lambda x:x*x
#value=f(5)
print('square of 5=', f(5))

# to print sum of two numbers
f=lambda x,y: x+y
value=f(10,5)
print('sum of two numbers=', value)

#maximum of two numbers
max= lambda x,y :x if x>y  else y
a,b=[int(n) for n in input("enter two numbers=").split(',')]
print('bigger number=', max(a,b))
