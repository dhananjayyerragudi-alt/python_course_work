"""
18/5/2026"""
"""
n=int(input("enter the number: "))
for i in range(n):
    for row in range (i+1):
        print(row+1, end=" ")
    print()
"""
"""
n=int(input("enter the number: "))
c=1
for i in range(n):
    for row in range(i+1):
        print(c, end=" ")
        c+=1
    print()
"""

"""
n=int(input("enter the number: "))

for i in range(n):
    for row in range(i+1):
        print(row*i, end=" ")
    print()

"""
"""

n=int(input("enter the number: "))

for i in range(n):
    for row in range(i+1):
        print(chr(65+row), end=" ")
        
    print()
"""
"""
n=int(input("enter the number: "))
c=0
for i in range(n):
    for row in range(i+1):
        print(chr(65+c),end=" ")
        c+=1
    print()
"""
"""
n=int(input("enter the number: " ))
for i in range(n):
    spaces=" "
    for row in range(i+1):
        print(spaces=" "*row+"*"*(2*row-1), end=" ")
    print()
    """
"""
"print max number using while loop"
l=[120,234,345,545,57, 83, 98,101]
i=0
m=0
while i<len(l):
    if l[i]>m:
        m=l[i]
    i+=1
print(m)
"""
""" print sum of both ends using while loop"
l=[120,220,36,42,545,67,724,83,98,101]
i=0
j=len(l)-1
while i<j:
    print(l[i]+l[j])
    i+=1
    j-=1
"""
    
""" list comprehension"""
'''
l=[1,2,3,4,5,6]

res=[i+10 for i in l]
print(res)
'''
""" mul value in a index with index"""
"""
l=[1,2,3,4,5,6]

res=[l[i]*i for i in range(len(l))]
print(res)

"""
""" find cubes in a value"""
"""
l=[1,2,3,4,5,6,7]
res=[i**3 for i in l]
print(res)
"""
"""print even number"""
"""
l=[1,2,3,4,5,6,7]
print(type(l))
res=[i for i in l if i%2==0]
print(res)
"""
"""
l=[1,2,3,4,5,6,7]
print(type(l))
res=[i if i%2==0 else 0 for i in 1]
print(res)
"""
n=int(input("Enter the number: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()