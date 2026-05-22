'''def greet(name):
    print(f"Hello{name}, welcome to python")
    

greet("Dhananjay")
'''
'''
def display(name,email,phonenumber):
    print(f'Name:{name}')
    print(f'email:{email}')
    print(f'phonenumber:{phonenumber}')
'''
'''

display("abc","abc@gmail.com","78793323232")
'''
'''

def display(name,email,phonenumber):
    print(f"Name:{name}")
    print(f"email:{email}")
    print(f"phonenumber:{phonenumber}")

display(name="def",email="def@gmail.com",phonenumber="7832231")
'''
'''
def display(name,email,phonenumber=None, cgpa=None):
    print(f"Name:{name}")
    print(f"email:{email}")
    print(f"phone Number:{phonenumber}")
    print(f"CGPA:{cgpa}")
    
display("avc","avc@gmail.com","78794613", 8.6)
'''
'''
def display(*names):
    print(names)
display("charan")
display("varun","dhanush")
'''
'''
def display(**names):
    print(names)
display(n1="charan")
display(n2="abc",n3="erere",n4="dasdf")
'''
'''
n=int(input("Enter the number: "))
c=0
for i in range(2,n//2+1):
    if n%i==0:
        c+=1
print("Prime Number" if c==0 else "Not prime number")
'''
'''
def isPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input("Enter the number: "))
print("Prime Number" if isPrime(n) else "Not Prime number")
'''
'''
def check_operations(s):
    digit=0
    vol=0
    con=0
    special_char=0
    word=1
    vow="aeiouAEIOU"
    
    for i in s:
        if i.isalpha():
            if i in vow:
                vol+=1
            else:
                con+=1
        elif i.isdigit():
            digit+=1
        elif i.isspace():
            word+=15
        else:
            special_char+=1
    print(f"vol_count: {vol}")
    print(f"con_count: {con}")
    print(f"dig_count: {digit}")
    print(f"spe_char: {special_char}")
    print(f"word_char: {word}")
s=input("Enter the word: ")
print(check_operations(s))
'''