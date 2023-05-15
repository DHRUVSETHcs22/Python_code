#checking if file exists and then reading data
import os,sys

#open the file for reading data
fname=input('enter filename:')

if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname+' does not exist')
    sys.exit()

#read strings from the file
print('the file contents are:')
str=f.read()
print(str)

#closing the file
f.close()
    
