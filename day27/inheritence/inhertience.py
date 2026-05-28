"""singleinheritence"""
"""
class A:
    def printa(self):
        print("Parent class- A")
class B(A):
    def printb(self):
        print("Child class-B")



a=A()
a.printa()
b=B()
b.printb()
b.printa()
"""
"""Hirarachial inheritence"""
"""
class A:
    def printa(self):
        print("Parent class- A")
class B:
    def printb(self):
        print("child class- B")
class C(A):
    def printc(self):
        print("child class - C")
class D(A):
    def printd(self):
        print("child class - D")

b=B()
b.printb()
b.printb()

c=C()
c.printc()
c.printa()
d=D()
d.printd()
d.printa()
"""
"""Multiple inheritence"""
"""
class A:
    def printa(self):
        print("Parent class- A")
class B:
    def printb(self):
        print("child class- B")
class C:
    def printc(self):
        print("child class - C")
class D(A,B,C):
    def printd(self):
        print("child class - D")
d=D()
d.printd()
d.printa()
d.printc()
d.printb()
"""
"""
class A:
    def printa(self):
        print("Parent class- A")
class B(A):
    def printb(self):
        print("child class- B")
class C(B):
    def printc(self):
        print("child class - C")
c=C()
c.printa()
c.printb()
c.printc()
"""
"""
class A:
    def printa(self):
        print("Parent class- A")
class B:
    def printb(self):
        print("child class- B")
class C(B,A):
    def printc(self):
        print("child class - C")
class D(C):
    def printd(self):
        print("child class - D")
d=D()
d.printd()
d.printa()
d.printc()
d.printb()
"""

"""Example"""
"""
class InstagramV1:
    def post(self):
        print("You can upload stories")
    def reel(self):
        print("You can upload reels")
class InstagramV2(InstagramV1):
    def story(self):
        print("You can upload stories")
    def live(self):
        print("You can go for the live")
class Whatsapp:
    def wpstatus(self):
        print("You can upload whatsapp status")
class Facebook:
    def fbstory(self):
        print("You can upload facebook story")

class InstagramV3(InstagramV2,Whatsapp,Facebook):
    def crossPlatforms(self):
        print("You can upload same story on your whatsapp status")
        print("You can upload same story on your facebook story")
sreeja=InstagramV1()
print("Sreeja-- Instagram V1")
sreeja.post()
sreeja.reel()

varun=InstagramV2()
print("Varun-- Instagram V2")
varun.post()
varun.reel()
varun.story()
varun.live()

charan=InstagramV3()
print("charan -- Instagram V3")
charan.post()
charan.reel()
charan.story()
charan.live()
charan.wpstatus()
charan.fbstory()
charan.crossPlatforms()
"""

"""
"super"
class A:
    def print(self):
        print("class-A")
class B(A):
    def print(self):
        super().print()
        print("class-B")
b=B()
b.print()
"""

class A:
    def print(self):
        print("class-A")
class B:
    def print(self):
        print("class-B")
class C(A,B):
    def print(self):
        A.print(self)
        B.print(self)
        print("class-c")
c=C()
c.print()
