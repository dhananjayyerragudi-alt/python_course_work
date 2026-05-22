'''
s="python"
for i in s:
    print(i)
'''
'''
s="python"
for i in enumerate(s):
    print(i[0],i[1])

'''
'''
l=[12345, 45678, 57878]

for i in enumerate(l):
    print(i[0],i[1])
'''
'''
d={"k1":"a","c":"b","e":"f"}
'''
'''
s="python"

for i in range(len(s)):
    print(i,s[i])
'''

'''
list1=["Abc","def","ghi","jkl"]

for i in range(len(list1)):
    print(i, list1[i])
'''
'''
pin=1234
for i in range(5):
    entered_pin=int(input("enter the pin: "))
    if entered_pin==pin:
        print("unlock the phone")
    else:
        print("invalid pin")
else:
    print("try after 60 sec")
'''
