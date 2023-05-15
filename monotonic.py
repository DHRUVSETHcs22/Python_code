s=0
j=1
ls=[65,55,43,42]
for i in range(0,len(ls)):
  if j !=4:
    if ls[i]>=ls[j]:
        s+=1
    j+=1
if s==len(ls)-1:
    print("True")
else:
    print("False")
