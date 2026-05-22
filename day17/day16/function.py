'''
def display(n):
    n=n+[5,6]
    print("inside the loop :" , n)
n=[1,2]
print(display(n))
print("outside the loop: ", n )
'''
'''
def display():
    global num
    num+=10
    print("inside the loop: ", num)
num=10
display()
print("outside the loop: ", num)
'''

def courses():
    course="Java"
    print("In the start: ", course)
    def change():
        nonlocal course
        course="python"
        print("changed:", course)
    change()
    print("Final:",course)
courses()

'''
s="python"
len=5
print(len)
'''
'''
def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)
'''
'''
def display(n):
    if n==11:
        return
    display(n+1)
    print(n)
display(1)
'''
'''
def display(s,ind):
    if ind==len(s):
        return
    display(s,ind+1)
    print(s[ind])

s="python"
display(s,0)
'''
'''
def display(s,ind):
    if ind==len(s)+1:
        return
    print(s[:ind])
    display(s,ind+1)
s="python programming"
display(s,0)
'''
'''
def display(s,ind,n):
    if ind==len(s)-n+1:
        return
    print(s[ind:ind+n])
    display(s,ind+1,n)
s="python"
display(s,0,5)
'''

def display(s):
    if s==11:
        return
    print()

s=10
display(10)
