#dictionary
#creating a dictionary using key value pairs

dict = {'Name':'Naman','ID':2015140014,'salary':89000}

#access value by giving key
print("name of employee = ",dict['Name'])
print("ID number = ",dict['ID'])
print("salary = ",dict['salary'])

n = len(dict)
print("no. of key value pair: ",n)

dict['salary'] = 90000
print(dict)

dict['dept'] = 'finance'
print(dict)

del dict['ID']
print(dict)
