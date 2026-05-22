Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
str1="Hello"
str2="World"
>>> str3="This is a multi_line string example"
>>> print(str1)
Hello
>>> print(str2)
World
>>> print(str3)
This is a multi_line string example
>>> str1+str2
'HelloWorld'
>>> str1+str2+str3
'HelloWorldThis is a multi_line string example'
>>> str1*3
'HelloHelloHello'
>>> print(str1[0])
H
>>> print(str1[1])
e
>>> print(str1[-1])
o
>>> print(str1[0:3])
Hel
>>> print(str2[:4])
Worl
>>> print("Hello" in str1)
True
>>> print("abc" in str1)
False
>>> print(str1)
Hello
>>> print(len(str1))
5
>>> print(max(str1))
o
>>> print(min(str2))
W
>>> print(chr(str2))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(chr(str2))
TypeError: 'str' object cannot be interpreted as an integer
