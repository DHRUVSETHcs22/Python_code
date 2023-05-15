#creating a dictionary from keyboard

x = {}

print("how many elements?" , end='')
n = int(input()) #indicates no. of key value pairs

for i in range(n):
    print("enter key:", end='')
    k = input()
    print("enter its value:", end='')
    v = int(input())
    x.update({k:v})

print("the dictionary is: ",x)
    
