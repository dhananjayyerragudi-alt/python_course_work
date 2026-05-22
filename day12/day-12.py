'''
l=[1,2,3,0,0,4,5,6,7,0,0,0,0,0,8,0,0,0,0,0]

while 0 in l:
    l.remove(0)

print(l)
'''
'''
i=1
while i<=10:
    print(i)
    i+=1
'''
'''
i=100
while i>=2:
    print(i)
    i-=2
'''
'''
n=int(input("Enter the number: "))
i=1
while i<=10:
    print(f'{n} * {i} = {n*i}')
    i+=1
'''
'''
i=1
while i<=10:
    i+=1
    if i==5:
        continue
    print(i)
        
'''
'''
n=int(input("Enter the number: "))
rem=0
while n>0:
        rem+=n%10
        n//=10
print(rem)
'''
"fact of given number"
'''
n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
'''

"factors of given number in the output"
'''
n=int(input("enter the number: "))

for i in range(1,n+1):
    if n%i==0:
        print(i, end=' ')
'''
"PROGRAM TO FIND THE NEXT LETTER OF STRING"
'''
n=input("enter the string:" )
new=""
for i in n:
    new+=chr(ord(i)+1)
print("New String: ", new)
'''
'''
n=input("Enter the string: ")
i=len(n)-1
while i >=0:
    print(n[i],i)
    i-=1
'''
'''
n=input("Ente the string: ")
for i in n:
    if n.count(i)==1:
        print(i)
        break
else:
    print("All characters are repeating multiple times")
'''
'''
n=int(input("Enter the number:" ))
rem=""
while n>0:
    rem+=str(n%10)
    n//=10
print(rem)
"OR"
'''
'''
n=int(input("Enter the number:"))
res=0
while n>0:
    rem=n%10
    res=res*10+rem
    n//=10
print(res,type(res))
'''
