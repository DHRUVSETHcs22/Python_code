math=int(input("enter maths no.=", ))
physics=int(input("enter physich no.=", ))
chemistry=int(input("enter chemistry no.=", ))
english=int(input("enter english no.=", ))
painting=int(input("enter painting no.=", ))
print("\n")
sum= (math+physics+chemistry+english+painting)
print("total marks obtained:", sum) 
print("\n")
per=sum//5
print("percentage obtained:", per )
print("\n")
if per==100 and per>=90 :
    print("you got 'O' grade")

elif per<90 and per>=80 :
    print("you got 'A+' grade")   

elif per<80 and per>=70 :
    print("you got 'A' grade")

elif per<70 and per>=60 :
    print("you got 'B' grade")

elif per<60 and per>=50 :
    print("you got 'B+' grade")     

else :
    print("you have failed in your exam")           
