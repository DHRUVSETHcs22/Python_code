keys=['ten','twenty','thirty']
values=[10,20,30]
dic={}
for i in range (0,len(keys)):
    dic.update({keys[i]:values[i]})
print(dic)
