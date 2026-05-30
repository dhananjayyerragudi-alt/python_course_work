"""polymorphism"""
"""
class Hotstar:
    def __init__(self,name):
        self.name=name
        print(f"Hello {self.name}, Welcome to the hotstar---")
    def login(self):
        print("You can login")
    def search(self):
        print("You can search")
    def categories(self):
        print("you can see the divisons")
    def playcontrollers(self):
        print("you can pause,resume and play")
    def livesports(self):
        print("you can watch sports on live")

    def ads(self):
        print("Add will run")
    def movies(self):
        print("limted movie")
    def downloads(self):
        print("Cant download")
    def quality(self):
        print("clrty will be decreased")

class PremiumUser(Hotstar):
    def __init__(self,name):
        self.name=name
        print(f"Hello {self.name}, welcome to the hotstar--")
    def ads(self):
        print("Add will not run")
    def movies(self):
        print("unlimted movie")
    def downloads(self):
        print("Can download")
    def quality(self):
        print("clrty will be high")

charan=Hotstar("charan")
charan.login()
charan.search()
charan.categories()
charan.playcontrollers()
charan.livesports()
charan.ads()
charan.movies()
charan.downloads()
charan.quality()
varun=PremiumUser("Varun")
varun.login()
varun.search()
varun.categories()
varun.playcontrollers()
varun.livesports()
varun.ads()
varun.movies()
varun.downloads()
varun.quality()
"""


""""""""""""""""""""""""""
"""operator overloading"""
"""
class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        return self.num+ other.num
    def __sub__(self,other):
        return self.num - other.num

a=Number(10)
b=Number(20)
print(a+b)
print(a-b)
"""

""""""""""""""""""""""""""


