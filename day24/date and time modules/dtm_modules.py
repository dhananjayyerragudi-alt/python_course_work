from datetime import date,time,datetime,timedelta
"""
t=date.today()
print(t)
print(t.year)
print(t.month)
print(t.day)
print(t.isoweekday())
"""
"""
print(date(2026,12,12))
"""
"""
year,month,day=list(map(int,input("enter the dob [YYYY-MM-D]:").split("-")))
print(year,month,day)
"""
"""
print(time(23,54,54))
"""
"""

n=datetime.now()
print(n.year)
print(n.hour)
print(n.minute)

n=datetime.now()
print(n.strftime("%Y/%M/%D"))
print(n.strftime("%y/%m/%d %I:%M:%S %p"))
"""

"""***Time delta***"""
n=datetime.now()
d=date.today()
a7=d-timedelta(days=20)
a15=n+timedelta(minutes=15)
print(a15)
print(a7)
