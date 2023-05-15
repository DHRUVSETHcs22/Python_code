#creating a file with strings
#open the file for writing data
f=open('myfile2.txt','w')

#enter strings from keyboard
print('enter text(@ at end):')
while str != '@':
    str=input() #accept sring into str
    #write the sring into file
    if(str!='@'):
        f.write(str+"\n")

#closing the file
f.close()
