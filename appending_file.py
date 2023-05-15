#appending and then reading strings
#open the file for reading data
f=open('myfile2.txt','a+')

#enter strings from keyboard
print('enter text to append(@ at end):')
while str != '@':
    str=input() #accept sring into str
    #write the sring into file
    if(str!='@'):
        f.write(str+"\n")

#put the file pointer to the beginning of file
f.seek(0,0)


#closing the file
f.close()
