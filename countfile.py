#counting number of lines,words and characters in a file
import os,sys

#open the file for reading data
fname=input('enter filename:')

if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname+' does not exist')
    sys.exit()

#initialize the counter to 0
cl=cw=cc=0

#read line by line from the file
for line in f:
    words=line.split()
    cl+=1
    cw+=len(words)
    cc+=len(line)

print('no. of lines:',cl)
print('no. of words:',cw)
print('no. of characters:',cc)

#close the file
f.close()








    
