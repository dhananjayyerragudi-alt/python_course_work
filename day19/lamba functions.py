add=lambda a,b:a+b
print(add(3,4))

square=lambda base,power:base**power
print(square(3,4))

wish=lambda name: f"{name}, welcome to the python"
print(wish("abc"))
print(wish("Def"))

"check whether number is even"
check=lambda num:"EVEN" if num%2==0 else "ODD"
print(check(19))
print(check(10))

"square"
square=lambda num:num**2
print(square(12))
"max"
check=lambda a,b: max(a,b)

print(check(100,101))

check=lambda a,b: a if a>b else b
print(check(1,3))

check=lambda s: len(s)
print(check("sfdgyuik"))

check =lambda s: "starts with vol" if s[0] in "aeiouAEIOU" else "not starts with vowel"
print(check("ewdefsg"))


check= lambda email:email.split("@")[-1]

print(check("abc@gmail.com"))

"leap year"
check=lambda year: "Leap pear" if year%400==0 or year%4--0 and year %100!=0 else "Not a leap year"
print(check(2016))

"square using map in lamba"
l=[1,2,3,4,5,6]
res=list(map(lambda i:i**2,l))
print(res)

x=["hello", "world", "python", "lambda"]
res=list(map(lambda i:i.upper(),x))
print(res)

l={'sahil':45, "niharika":80,"mounika":65,"charan":92}
print(dict(sorted(l.items(),key=lambda i:i[1])))
print(dict(sorted(l.items(),key=lambda i:i[1],reverse=True)))

x=[1,2,3,4,5]
res=list(map(lambda i:i-10,x))
print(res)
