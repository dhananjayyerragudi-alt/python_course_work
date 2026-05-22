

"1"
'''
a=int(input("Enter A ",))
b=int(input("Enter B ",))
c=int(input("Enter C ",))
if a==b==c:
    print("Equilateral")
elif (a==b!=c or a!=b==c or c==a!=b):
    print("Isosceles")
else:
    print("Scalene")
'''
"2"
'''
char=input("Enter the char: ",)
vow=("a","e","i","o","u","A","E","I","O","U")
const=("b","c","d",)
if char in vow:
    print("Vowel")
elif char not in vow:
    print("Consonant")
elif int(char).isalpha():
    print("digit")
else:
    print("special character")
'''
"3"
'''
units=int(input("Enter the units ",))
if 0<=units>=100:
    units=units*1
    print("cost in rupess: ", units )

elif 100<=units>=200:
    print("cost in rupess: ", units*2)
    
else:
    
    print("cost in rupess:", units*3)
'''
"30"
'''
number=input("Enter the number: ",)

if len(number)==10 and number[0]=="6" or number[0]=="7" or number[0]=="8" or number[0]=="9":
    print("Valid")
else:
    print("Invalid")
'''
"29"
'''
num1=int(input("Enter the number: ",))
num2=int(input("Enter the number: ",))
num3=int(input("Enter the number: ",))
if num1<num2<num3:
    print("Improving")
else:
    print("Declining")
'''
"28"
'''
num1=int(input("Number of classes attended: ",))

if num1>=75:

    print("Valid")
else:
    print("invalid")

  '''
"27"  
'''
Day_type=int(input("Enter the number: ",))
if Day_type==1:
    print("Monday- Weekday")
elif Day_type==2:
    print("Tuesday-Weekday")
elif Day_type==3:
    print("Wednesday-weekday")
elif Day_type==4:
    print("Thursday-weekday")
elif Day_type==5:
    print("Friday-weekday")
elif Day_type==6:
    print("saturday-weekday")
else:
    print("Sunday-weekend")
'''
"25"
'''
plan=int(input("Enter the plan:", 
               ))
if plan<1:
    print("Plan A")
elif plan<5:
    print("Plan B")
else:
    print("Plan C")
'''   
"24"
'''
num=int(input("enter the value: ",))
if num<10:
    print("very cold")
elif num>=10 and num<=20:
    print("Cold")
elif num>=21 and num<=30:
    print("warm")
else:
    print("Hot")           
'''

"22"
'''
num=input("enter the value: ",)
if len(num)==1:
    print("single digit")
elif len(num)==2:
    print("double digit")
else:
    print("triple digit")
'''
"21"
'''
age=int(input("enter the age: ",))
if age<12:
    print("50")
elif age<60:
    print("100")
else:
    print("60")
'''
"20"
'''
age=int(input("enter the age: ",))
exp=int(input("enter the experience: ",))
if age< 25 and exp < 3:
    print("High risk")
else:
    print("Low risk")
'''
"19"
'''
num=input("Enter the number: ",)
while len(num)==3:
    x=int(num)
    x=x//10 
print(x)
'''

"8"
'''
num=int(input("Enter the number: ,"))
base_fare=100 
if num<5:
    print("0")
elif num<18:
    print(base_fare-(50))
elif 18<num<60:
    print("No discount")
else:
    print(base_fare-(30))
'''

"11"
'''
num=int(input("Enter the number: "))
if 90<=num<=100:
    print("A")
elif 85<=num<=89:
    print("B+")
elif 80<=num<=84:
    print("B")
elif 70<=num<=79:
    print("C")
else:
    print("F")
'''
"BMI"
'''
weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))
height_m = height_cm / 100

bmi = weight / (height_m ** 2)
        
bmi_rounded = round(bmi, 2)

if bmi < 18.5:
    print("Status: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Status: Healthy weight")
elif 25 <= bmi < 29.9:
    print("Status: Overweight")
else:
    print("Status: Obese")
'''
"electricity"
'''
units=int(input("Enter the number: "))
if 0<=units<=100:
    print(units*1)
elif 101<=units<=200:
    print(units*1+(units-100)*2)
else:
    print(units*1+units*2+(units-200)*3)
'''