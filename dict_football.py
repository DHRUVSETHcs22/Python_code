#creating a dictionary with football player names and scores

x = {} #empty dictionary

print("how many elements:",end='')
n = int(input())

for i in range(n):
    print("enter the player name:",end='')
    k = input()
    print("enter goal scored:",end='')
    v = int(input())
    x.update({k:v})

#display only player names
print("players in the match:",x.keys())

#accept a player from the keyboard
print("enter player name:",end='')
name = input()

#find goals scored by player
goals = x.get(name,-1)
if(goals == -1):
    print("player not found")
else:
    print("{} scored {} goals.".format(name,goals))

    
        

