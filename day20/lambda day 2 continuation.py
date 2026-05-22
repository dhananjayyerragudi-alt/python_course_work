
"""20-5-26"""
"""lambda"""
'''
l=[1,2,3,4,5,6,7,8]
res=list(filter(lambda i:i%2==0,l))
print(res)
l=[1,2,3,4,5,6,7,8,9]
res=list(filter(lambda i:i%2!=0,l))
print(res)
l="python programming language"
res=list(filter(lambda i : i in 'aieou',l ))
print(res)

x=["operators","conditional","control","oops","files","exeception"]
res=list(filter(lambda i: i[0] not in "aeiouAEIOU",x))
print(res)

x=["operators","conditional","control","oops","files","exeception"]
res=list(filter(lambda i: len(i)>8, x))
print(res)


data={
    'dell':{'stock':0,'price':89000},
    'lenovo':{'stock':15, 'price':55000},
    'mac':{'stock':8,'price':120000},
    'hp':{'stock':12, 'price':45000},
    'thinkpad':{'stock':0,'price':37000}
    }
res=list(filter(lambda i:data[i]['price']>50000,data))
print(res)

'''
'''

data={
    'dell':{'stock':0,'price':89000},
    'lenovo':{'stock':15, 'price':55000},
    'mac':{'stock':8,'price':120000},
    'hp':{'stock':12, 'price':45000},
    'thinkpad':{'stock':0,'price':37000}
    }
res={i:data[i]['price'] for i in data}
x2h=dict(sorted(res.items(),key=lambda i:i[1]))
h2x=dict(sorted(res.items(),key=lambda i:i[1],reverse=True))
print("Low to high:")
print(x2h)
print("high to low:")
print(h2x)
'''
""" reduce function"""
'''
from functools import reduce
m=['operators','control','conditional','oops','files','exception']
l=[1,2,3,4,5,6,7,8]
ms=reduce(lambda sum,i:sum+','+i,m)
s=reduce(lambda sum, i:sum+i, l)
p=reduce(lambda pro, i:pro*i, l)
print(ms,s,p)
'''
"Generators"
'''
def reels():
    r=['1..100','2..200','3...300','4..400','5..500']
    for i in r:
        yield i
scroll=reels()
print(next(scroll))
print(next(scroll))

print(next(scroll))

print(next(scroll))
'''
'''
def reels():
    yield "1-10 files"
    yield "11-20 files"
    yield "21-30 files"
    yield "31-40 files"
    yield "41-50 files"
scroll=reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))

print(next(scroll))
'''
