'''
x=int(input("Enter the number: "))
if x%2==0:
    print("4-digit even number")
   '''
'''
x=input("Enter the letter: ")
vowels=["a","e","i","o","u","A","E","I","O","U"]
if x not in vowels:
    print(x,"is consonant")
else:
    print(x,"is not consonant")
'''
'''
x=int(input("enter the number: "))
if x%2==0 and x%3==0:
    print(x, "Divisible by both 2 and 3")
else:
    print(x, "Divisible by 2 only")
'''
'''
x=int(input("enter the number: "))
if x<0 and x%2==1:
    print("Negative and odd number")
else:
    print("Not Negative and odd number")
'''

x=input("enter the number: ")
vowels=["a","e","i","o","u","A","E","I","O","U"]
if x[0] in vowels:
    print("starts with a vowel")
else:
    print("doesn't start with a vowel")

