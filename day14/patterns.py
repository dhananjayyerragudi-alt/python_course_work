'''patterns'''
''' * (star) patterns '''
'''
n=int(input("Enter the number: "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

'''
'''
n=int(input("Enter the number: "))
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
'''
'''
n=int(input("Enter the number: "))
for i in range(n):
    for space in range(n-i-1):
        print("# ", end=" ")
    for j in range(i+1):
        print("* ", end=" ")
    print()
'''
'''
n=int(input("enter the number: "))
for i in range(n):
    for space in range(i):
        print("  ", end= " ")
    for j in range(n-i):
        print("* ", end=" ")
    print()
'''
'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if col%2==0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
'''
'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if col%2!=0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
'''
'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if (row+col)%2==0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
'''
'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if (row+col)%2!=0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
'''
'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==(n-1) or col==0 or col==(n-1):
            print("* ", end=" ")
        else:
            print("  ", end=" ")
            
    print()
'''
'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==(n-1) or col==0 or col==(n-1):
            print("* ", end=" ")
        elif n//2==row or n//2==col:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
            
    print()
'''
'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==(n-1) or row+col==(n-1):
            print("* ", end=" ")
        else:
            print("  ", end=" ")
            
    print()
'''
'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if row==col or row+col==(n-1):
            print("* ", end=" ")
        else:
            print("  ", end=" ")
            
    print()
'''
"1"
'''
n=int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
'''
"2"
'''
row=int(input("enter the number: "))
col=int(input("enter the number: "))
for i in range(row):
    for j in range(col):
        print("*",end=" ")
    print()
'''
"3"
'''
n=int(input("enter the number: "))

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
'''
"4"
'''
n=int(input("enter the number: "))
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
'''
"9"
'''
n=int(input("enter the number: "))
for i in range(n):
    print("* " * 1 )
'''
"10"
'''
n=int(input("enter the number: "))
for i in range(n):
    print("*"*1, end=" ")
'''