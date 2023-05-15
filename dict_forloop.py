#using for loop with dictionary

colors = {'r':"red",'g':"green",'b':"blue",'w':"white"}

#display only keys
for k in colors:
    print(k)

#pass keys to dictionary and display the values
for k in colors:
    print(colors[k])

#items() method return key and value pair into k,v
for k,v in colors.items():
    print("key= {} values= {}".format(k,v))
