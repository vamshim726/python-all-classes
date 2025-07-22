

'''
Abstraction:
Hiding the implementation details, showing required things

consider example : payment gateway
the skelton will be shared - no full code to the user(upi,creditcard,netbanking)

- abstract class has  no implementation methods
- cannot create the objects for abstract class
- in abstract class there will be abstract methods or normal methods
-we have to inhert to do our own implementation
- if we inhert from abstract class , then we have to create object to that class
    - we have to implement all the abstract methods
    - if we dont implemnt the that class also become the abstract class
    - the implemented class is called concrete class
'''

from abc import ABC, abstractmethod

class PaymentProcess(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

    def print_details(self):
        print('')



class UPI(PaymentProcess):

    def pay(self,amount):
        print(amount,'money payed using UPI')
class DebitCard(PaymentProcess):

    def pay(self,amount):
        print(amount,'money payed using Debit Card')

class NetBanking(PaymentProcess):

    def pay(self,amount):
        print(amount,'money payed using Net Banking')



p=UPI()
p.pay(5000)