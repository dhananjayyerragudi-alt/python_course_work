'''
discount= int(input("Enter the discount: "))
price=int(input("Enter the price: "))

if discount:
    price-=price*(discount/100)
    print("Discount applied")
    print("price",price)
else:
    print("No discount applied")
'''
'''
data = {'abc@gmail.com':'123',
        'xyz@gmail.com':'456',
        'hef@gmail.com':'789'}
email= input("Enter the email: ")
password=input("Enter the password: ")

if data.get(email)==password:
    print("Login successfull")
else:
    print("Login invalid")
'''
'''
x=5
if x>0:
    print("It is positive")
else:
    print("Negative")
'''
'''
import random
otp= random.randint(1111,9999)
print("Your OTP", otp)
entered_otp=int(input("enter the otp: "))
if otp== entered_otp:
    print("verified successfully")
else:
    print("invalid otp")
'''
'''
hr,min=list(map(int, input("Enter the time(HH:MM): "). split(':')))
fare=0
price=350
if 0<=hr<=23 and 0<=min<=59:
    if 8<=hr<=16:
        fare=40
    elif 17<=hr<=23:
        fare=100
    elif 0<=hr<-7:
        fare=150
    print("Total fare:", fare+price)
else:
    print("invalid time")
'''
