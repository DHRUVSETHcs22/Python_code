# mini calculator

a=input("enter the first value : ")
c=input("enter the valid operator(+,-,*,/) : ")
b=input("enter the second value : ")

if c in'+' :
   print("a+b =",int(a)+int(b))
   
elif c in '-' : 
    print("a-b =",int(a)-int(b))

elif c in '*' :
    print("a*b =",int(a)*int(b))

elif c in '/':
    print("a/b =",int(a)/int(b))

else :
    print("operator is wrong please valid operator")       