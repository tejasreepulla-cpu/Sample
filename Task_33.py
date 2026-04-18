"""Polymorphism:implementing same thing in different forms
There are 2 types:
    1.Overloading:method should be same name but different arguments i.e in the terms of length/type of arguments
        1.Operator Overloading
        2.Method Overloading
    2.Method Overriding:method should be same name and arguments should also be same length"""
    
# 1.Operator Overloading:(+)
# a=10
# b=20
# print(a+b)

# a="kiran"
# b="kumar"
# print(a+b)

# 2.Method Overloading:
# class calculator():
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj=calculator()
# obj.add(10,10) #Type Error
# obj.add(10,10,20)
# obj.add(25,25) #Type Error

# class calculator():
#     def add(self,a,b,c):
#         print(a,b,c)
# obj=calculator()
# obj.add(10,10,10)
# obj.add(10,10) #Type Error
# obj.add(10) #Type Error
# obj.add() #Type Error
# obj.add("althaf",25,1234)
# obj.add("raju",15,) #Type Error
# obj.add("kiran",) #Type Error
# obj.add() #Type Error

# class calculator():
#     def add(self,a=None,b=None,c=None):
#         print(a,b,c)
# obj=calculator()
# obj.add(10,10,10)
# obj.add(10,10)
# obj.add(10)
# obj.add()
# obj.add("althaf",25,1234)
# obj.add("raju",15,)
# obj.add("kiran",)
# obj.add()

# 2.Method Overriding:
# class gfather():
#     def details(self,a):
#         print(f"this is gfather class {a}")
# class father(gfather):
#     def details(self,a):
#         print(f"this is father class {a}")
# obj=father()
# obj.details(100)


# To access the base class attributes and methods we will use super() class
# class gfather():
#     def details(self,a):
#         print(f"this is gfather class {a}")
# class father(gfather):
#     def details(self,a):
#         print(f"this is father class {a}")
#         super().details("100cr")
# obj=father()
# obj.details(100)

"""Encapsulation:mechanism of wrapping the data(variables) and code acting on the data(methods) together as a single unit
We can provide security to the data by using access modfiers i.e 1.public(Accessible to outside world 2.protected(Accessible to derived classes 3.private(Not accessible to outside world)))"""
# 1.public:

# class gfather():
#     def __init__(self,a):
#         self.a=a
#         print(f"this is base class {a}")
# class father(gfather):
#     def details(self):
#         print(f"this s father class {self.a}")
# obj=father("100cr")
# obj.details()

# 2.protected

# class gfather():
#     def __init__(self,a):
#         self._a=a
#         print(f"this is base class {a}")
# class father(gfather):
#     def details(self):
#         print(f"this is father class {self.a}")
# obj=father("100cr")

# class gfather():
#     def __init__(self,a):
#         self._a=a
#         print(f"this is base class {a}")
# class father(gfather):
#     def details(self):
#         print(f"this is father class {self.a}")
# obj=father("100cr")
# obj.details() #Attribute error

# class gfather():
#     def __init__(self,a):
#         self._a=a
#         print(f"this is base class {a}")
# class father(gfather):
#     def details(self):
#         print(f"this is father class {self._a}")
# obj=father("100cr")
# obj.details()

# 3.Private

# class gfather():
#     def __init__(self,a):
#         self.__a=a
#         print(f"this is base class {a}")
# class father(gfather):
#     def details(self):
#         print(f"this s father class {self.a}")
# obj=father("100cr")

# class gfather():
#     def __init__(self,a):
#         self.__a=a
#         print(f"this is base class {a}")
# class father(gfather):
#     def details(self):
#         print(f"this s father class {self._a}")
# obj=father("100cr")
# obj.details() #Attribute error

# class gfather():
#     def __init__(self,a):
#         self.__a=a
#         print(f"this is base class {a}")
# class father(gfather):
#     def details(self):
#         print(f"this s father class {self.__a}")
# obj=father("100cr")
# obj.details()

# Data Abstraction:hiding the implementation and showing only essential part.

# from abc import ABC,abstractmethod
# class abstract_demo(ABC):
#     @abstractmethod
#     def display(self):
#         pass
#     @abstractmethod
#     def display2(self):
#         pass
# class demo(abstract_demo):
#     def display(self):
#         print(f"implementation done")
#     def display2(self):
#         print(f"implementation 2 done")
# obj=demo()
# obj.display()
# obj.display2()

# from abc import ABC,abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def payment(self):
#         pass
# class gpay(payment):
#     def payment(self):
#         print(f"Payment received via gpay")
# class phonepe(payment):
#     def payment(self):
#         print(f"Payment received via phonepe")
# class paytm(payment):
#     def payment(self):
#         print(f"Payment received via paytm")
# class crud(payment):
#     def payment(self):
#         print(f"Payment received via crud")
# obj=gpay()
# obj.payment()
# obj2=phonepe()
# obj2.payment()
# obj3=paytm()
# obj3.payment()
# obj4=crud()
# obj4.payment()

# from abc import ABC,abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def payment(self):
#         pass
# class gpay(payment):
#     def payment(self):
#         print(f"Payment received via gpay")
# class phonepe(payment):
#     def payment(self):
#         print(f"Payment received via phonepe")
# class paytm(payment):
#     def payment(self):
#         print(f"Payment received via paytm")
# class crud(payment):
#     def payment(self):
#         print(f"Payment received via crud")
#     def cashback(self):
#         print(f"1% cashback upto 10rs/-")
# obj=gpay()
# obj.payment()
# obj2=phonepe()
# obj2.payment()
# obj3=paytm()
# obj3.payment()
# obj4=crud()
# obj4.payment()
# obj4.cashback()

# from abc import ABC,abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def payment(self,a):
#         pass
# class gpay(payment):
#     def payment(self,a):
#         print(f"Payment received via gpay {a}")
# class phonepe(payment):
#     def payment(self,a):
#         print(f"Payment received via phonepe {a}")
# class paytm(payment):
#     def payment(self,a):
#         print(f"Payment received via paytm {a}")
# class crud(payment):
#     def payment(self,a):
#         print(f"Payment received via crud {a}")
#     def cashback(self):
#         print(f"1% cashback upto 10rs/-")
# obj=gpay()
# obj.payment(100)
# obj2=phonepe()
# obj2.payment(200)
# obj3=paytm()
# obj3.payment(300)
# obj4=crud()
# obj4.payment(400)
# obj4.cashback()



        


