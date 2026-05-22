"""def isprime(num):
    res=[]
    for i in range(2,num+1):
        for j in range(2,i//2+1):
            if i%j==0:
                break
            else:
                res.append(i)
    return res
def generators(res):
    for i in res:
        yield i 
def calling(p):
    g=generators(p)
    for i in range(len(p)):
        print(g(p))

isprime(10)
"""

"generate factors"
"""
def factors(n):
    res=[]
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return res

def generators(res):
    for i in res:
        yield i

r=factors(38)
g=generators(r)
for i in range(len(r)):

    print(next(g))
"""
""" list reverse order"""
"""
def generators(res):
    for i in range(len(res)-1,-1,-1):
        yield res[i]

l=[1,2,3,4,5,6,7,8]
g=generators(l)
for i in range(len(l)):
    print(next(g),end=" ")
"""
"""
def even(l):
    return list(filter(lambda i:i%2==0,l))
def gen(l):
    for i in l:
        yield i
l=[1,2,43,4,43,4,4,65,6766,7867,7122,2322,565,566]

e=even(l)
g=gen(e)
for i in range(len(e)):
    print(next(g))
"""
"""recursion"""
"""factorial"""
"""
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(12))
"""
"""
def count(n):
    if n==0:
        return 0
    
    return 1+ count(n//10)
print(count(1234789))
"""
        
