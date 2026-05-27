"""
class Flipkart:
    products={"laptop":987654,
              "phone":89765,
              "earphones":854,
              "bags":123}
    @classmethod
    def showProducts(cls):
        print(cls.products)

    def register(self,name,phno):
        self.username=name
        self.phonenumber=phno
        print(f"welcome to flipkart(self.username),shop now!!!")
    @staticmethod
    def discount():
        print("Hey all, 10% discount is going on, shop now!!!")

charan=Flipkart()
charan.register("charan","9876543210")
charan.discount()
charan.showProducts()

"""
"""constructor example"""
"""
class Flipkart:
    def __init__(self,name,phno):
        self.username=name
        self.phonenumber=phno
        print(f"welcome to flipkart {self.username} ,shop now!!!")
charan=Flipkart("Djay","987654321")
"""

