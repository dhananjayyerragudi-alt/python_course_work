Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x=input()
b
print(x)
b
x=int(input())

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x=int(input())
ValueError: invalid literal for int() with base 10: ''
length=5
type(length)
<class 'int'>
int_a=2
float(int_a)
2.0
>>> str(int_a)
'2'
>>> bool(int_a)
True
>>> list(int_a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    list(int_a)
TypeError: 'int' object is not iterable
>>> set(int_a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    set(int_a)
TypeError: 'int' object is not iterable
>>> tuple(int_a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    tuple(int_a)
TypeError: 'int' object is not iterable
>>> dict(int_a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    dict(int_a)
TypeError: 'int' object is not iterable
>>> float_n=3.1
>>> int(float_n)
3
>>> str(float_n)
'3.1'
>>> bool(float_n)
True
>>> list(float_n)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list(float_n)
TypeError: 'float' object is not iterable
>>> set(float_n)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    set(float_n)
TypeError: 'float' object is not iterable
