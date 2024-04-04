#Traffic light code
"""Light=input("Light :")
if(Light=="red"):
    print("stop")
elif(Light=="green"):
    print("go")
elif(Light=="yellow"):
    print("slow speed")
else:
    print("Light not work")


print("*********practice********")"""


"""A=int(input("A:"))
G=input("M/F:")
if((A==1 or A==2) and G=="M"):
    print("Fee is 100")
elif(A==3 or A==4 or G=="F"):
    print("fee is 200")
elif(A==5 or G=="M"):
    print("fee is 300")
else:
    print("No fee")"""

print("single line if_else conditional statement")
# <var>=<val>if<condition>else<val2>
"""food=input("food:")
eat="yes" if food=="cake" else "no"
print(eat)"""

#<stat1>if<condition>else<statement>
"""food=input("food:")
print("sweet")if food=="jalebi" or food=="barfi" else print("not sweet")"""

#clever if /ternary operator
#<var>=(false,true)[condition]
age=int(input("age:"))
vote=("yes","No") [age<18]
print(vote)
