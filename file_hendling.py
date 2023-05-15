
f=open("file1.txt",'r')
i=0
while True :
    line=f.readline()
    if line :
        i+=1
    else:
        break
print("no. of lines present in file:",i)
f.seek(0)
word = f.readline()
print("no. of words present in file:",len(word))
f.seek(0)
i=0
z=0
while True:
    w=f.read()
    if w:
        w=list(w)
        for j in w:
            if j<('z') and j>('a') or j<'Z' and j>'A':
                i+=1
            else:
                if j!='/n':
                   z+=1
    else :
        break
print("no. of characters present in file:",i)
print("no. of spaces:",z)
f.close()
