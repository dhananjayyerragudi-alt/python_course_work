from abc import ABC,abstractmethod

class PhonePay(ABC):
    def input(self):
        print("You can scan or enter the number")
    def amount(self):
        print("You the amount to pay")
    def pin(self):
        print("You can enter the pin")

    @abstractmethod

    def verification(self):
        pass
    def paymentstatus(self):
        print("You amount the transferred successfully/failed")

class HDFC(PhonePay):
    def verification(self):
        print("Verification is successfuly through HDFC")
class SBI(PhonePay):
    def verification(self):
        print("Verification is successfully through SBI")

class AXIS(PhonePay):
    def verification(self):
        print("Verification is successfully through AXIS")

charan=HDFC()
charan.input()
charan.amount()
charan.pin()
charan.verification()
charan.paymentstatus()

varun=SBI()
varun.input()
varun.amount()
varun.pin()
varun.verification()
varun.paymentstatus()

prince=SBI()
prince.input()
prince.amount()
prince.pin()
prince.verification()
prince.paymentstatus()

