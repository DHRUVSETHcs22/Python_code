a=input("enter a sentence:", )
x=0
z=0
i=0

while(i<len(a)):

    if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U'):
          x+=1
            
    else:
          z+=1
             
    i+=1 
         

print("no. of vowiles:",x)
print("\n")
print("no. of consonant:",z)        

  