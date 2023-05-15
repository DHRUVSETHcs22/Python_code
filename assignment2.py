''' 
print(20>30) #Ans = flase


print(True>2) #ans = false


print("Abc"=="abc") #Ans= false


print(10 or 20) #Ans= 10


print(0 or False) #Ans = false


print("abc" or "xyz") #Ans = abc


print(True<<1) #Ans = 2


print(~5) #Ans = -6


print(bin(10)) #Ans = 0b1010


print(oct(10)) #Ans = 0o12


print(hex(10)) #Ans = 0xa


a=10>5
print(a) #Ans = True


n1=0o17
n2=0b1110010
n3=0x1c2
n=int(n1)
print(n)#Ans = 15
n=int(n2)
print(n)#Ans = 114
n=int(n3)
print(n)#Ans = 450


n=int(input())
print(bin(n)[2:])#Ans = 2 =10


n=input("enter a binarry no.")
m=input("enter another binarry no.")
x=int(n,2) + int(m,2)
y=bin(x)
print(y) #Ans = 0b10011010
print(y[2:]) #Ans = 10011010


n=int(input("enter a dight:"))
if(n & (n-1))==0:
    print("Yes")      #Ans = 5 =No ; 2=Yes
else:
    print("No")    


x=int(input())
y=int(input())
x=x^y
y=x^y           #Ans = intput(x=5 ; y=2) = output(x=2 : y=5 )
x=x^y         
print(x,y)

'''

