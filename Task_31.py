# OOPs:
# class personal_details:
#     user_name="raju"
#     user_id=12345
#     def details(self):
#         print(f"Working at ABC company {self.user_name}")
#     def details_2(self):
#         print(f"he runs ABC company {self.user_id}")
# ramu=personal_details()
# ramu.details()
# ramu.details_2()
# print(ramu.user_id)
# print(ramu.user_name)

# class personal_details:
#     user_name="raju"
#     user_id=12345
#     def details(self):
#         print(f"Working at ABC company {self.user_name}")
#     def details_2(self):
#         print(f"he runs ABC company {self.user_id}")
#         self.details()
# ramu=personal_details()
# ramu.details_2()

# class feature_phone():
#     brand_name="Nokia"
#     colour="White"
#     model=2006
#     def calling(self):
#         print(f"you are calling...")
#     def message(self,mn):
#         print(f"message sent from {self.brand_name} successfully to {mn}...")
# nokia=feature_phone()
# nokia.calling()
# nokia.message(123456789)
# nokia_2016=feature_phone()
# nokia_2016.calling()
# nokia_2016.message(98765443322)
# microsoft=feature_phone()
# microsoft.calling()
# microsoft.message(987656789)

# class feature_phone():
#     brand_name="Nokia"
#     colour="White"
#     model=2006
#     def calling(self):
#         print(f"you are calling...{self.brand_name}")
#     def message(self,mn):
#         print(f"message sent from {self.brand_name} successfully to {mn}...")
# nokia=feature_phone()
# nokia.calling()
# nokia.message(123456789)
# nokia_2016=feature_phone()
# nokia_2016.calling()
# nokia_2016.message(98765443322)
# microsoft=feature_phone()
# microsoft.calling()
# microsoft.message(987656789)

# class feature_phone():
#     brand_name="Nokia"
#     colour="White"
#     model=2006
#     def calling(self,bn):
#         print(f"you are calling...{bn}")
#     def message(self,mn):
#         print(f"message sent from {self.brand_name} successfully to {mn}...")
# nokia=feature_phone()
# nokia.calling("nokia")
# nokia.message(123456789)
# nokia_2016=feature_phone()
# nokia_2016.calling("nokia_2016")
# nokia_2016.message(98765443322)
# microsoft=feature_phone()
# microsoft.calling("microsoft")
# microsoft.message(987656789)

# class feature_phone():
#     def __init__(self,bn,color,model):
#         self.bn=bn
#         self.color=color
#         self.model=model
#     def calling(self,):
#         print(f"you are calling...{self.bn}")
#     def message(self,mn):
#         print(f"{self.model} message sent successfully to {mn}...")
# samsung=feature_phone("Samsung","white",2016)
# samsung.calling()
# samsung.message(123456789)

# class feature_phone():
#     def __init__(self,bn,color,model=2006):
#         self.bn=bn
#         self.color=color
#         self.model=model
#     def calling(self,):
#         print(f"you are calling...{self.bn}")
#     def message(self,mn):
#         print(f"{self.model} message sent successfully to {mn}...")
# samsung=feature_phone("Samsung","white")
# samsung.calling()
# samsung.message(123456789)
# nokia=feature_phone("Nokia","black",2007)
# nokia.calling()
# nokia.message(123456789)

# class feature_phone():
#     def __init__(self,bn,color,model=2006):
#         self.bn=bn
#         self.color=color
#         self.model=model
#     def calling(self,):
#         print(f"you are calling...{self.bn}")
#     def message(self,mn):
#         print(f"{self.model} message sent successfully to {mn}...")
# class smart_phone(feature_phone):
#     def __init__(self,ram,battery):
#         self.ram=ram
#         self.battery=battery
#     def capture(self):
#         print(f"you are capture")
#     def browsing(self,browser):
#         print(f"you are browsing from {browser}")
# samsung=smart_phone("Samsung","white","2014","8gb","50000mah")
# print(samsung.bn)
# print(samsung.color)
# print(samsung.model)
# print(samsung.ram)
# print(samsung.battery)   #Type error

# single Inheritance:
# class feature_phone():
#     def __init__(self,bn,color,model,ram,battery):
#         self.bn=bn
#         self.color=color
#         self.model=model
#         self.ram=ram
#         self.battery=battery
#     def calling(self,):
#         print(f"you are calling...{self.bn}")
#     def message(self,mn):
#         print(f"{self.model} message sent successfully to {mn}...")
# class smart_phone(feature_phone):
#     def capture(self):
#         print(f"you are capture")
#     def browsing(self,browser):
#         print(f"you are browsing from {browser}")
# samsung=smart_phone("Samsung","white","2014","8gb","50000mah")
# print(samsung.bn)
# print(samsung.color)
# print(samsung.model)
# print(samsung.ram)
# print(samsung.battery)
# samsung.calling()
# samsung.capture()
# samsung.browsing("chrome")
# samsung.message(123456)

# class feature_phone():
#     def __init__(self,bn,color,model,ram,battery):
#         self.bn=bn
#         self.color=color
#         self.model=model
#         self.ram=ram
#         self.battery=battery
#     def calling(self,):
#         print(f"you are calling...{self.bn}")
#     def message(self,mn):
#         print(f"{self.model} message sent successfully to {mn}...")
# class smart_phone(feature_phone):
#     def __init__(self,bn,color,model,ram,battery):
#         self.bn=bn
#         self.color=color
#         self.model=model
#         self.ram=ram
#         self.battery=battery
#     def capture(self):
#         print(f"you are capture")
#     def browsing(self,browser):
#         print(f"you are browsing from {browser}")
# samsung=smart_phone("Samsung","white","2014","8gb","50000mah")
# print(samsung.bn)
# print(samsung.color)
# print(samsung.model)
# print(samsung.ram)
# print(samsung.battery)
# samsung.calling()
# samsung.capture()
# samsung.browsing("chrome")
# samsung.message(123456)

# Hierarchical Inheritance:
# class a():
#     def parent(self):
#         print(f"this is parent class")
# class b(a):
#     def child1(self):
#         print(f"this is child1 class")
# class c(a):
#     def child2(self):
#         print(f"this is child2 class")
# obj=b()
# obj.child1()
# obj.parent()
# obj_1=c()
# obj_1.child2()
# obj_1.parent()

# Multiple Inheritance
# class parent1():
#     def father(self):
#         print("this is father class")
# class parent2():
#     def mother(self):
#         print("this is mother class")
# class child(parent1,parent2):
#     def child(self):
#         print("this is child class")
# obj=child()
# obj.child()
# obj.father()
# obj.mother()


#Multilevel Inheritance
# class gfather():
#     def output(self):
#         print(f"earned 100cr properties")
# class father(gfather):
#     def output1(self):
#         print(f"this is father class")
# class child(father):
#     def output2(self):
#         print(f"this is child class")
#     def sample(self):
#         print(f"started ABC company")
# obj=child()
# obj.output2()
# obj.sample()
# obj.output1()
# obj.output()

# Laptop program
# class Laptop():
#     def __init__(self,brandname,colour,size,storage):
#         self.brandname=brandname
#         self.colour=colour
#         self.size=size
#         self.storage=storage
#     def on_laptop(self):
#         print(f"{self.brandname} laptop is opened")
#     def off_laptop(self):
#         print(f"{self.brandname} laptop is closed")
#     def music(self,language):
#         print(f"Laptop is playing {language} music")
#     def browsing(self,browser):
#         print(f"you are browsing from {browser}")
#     def gaming(self,name):
#         print(f"I am playing {name}")
# hp=Laptop("hp","ash","14inches","128gb")
# print(hp.brandname)
# print(hp.colour)
# print(hp.size)
# print(hp.storage)
# hp.on_laptop()
# hp.off_laptop()
# hp.music("karnatak")
# hp.gaming("Ludo")
# hp.browsing("Chrome")
# dell=Laptop("dell","black","15inches","256gb")
# print(dell.brandname)
# print(dell.colour)
# print(dell.size)
# print(dell.storage)
# dell.on_laptop()
# dell.off_laptop()
# dell.music("kerala")
# dell.gaming("pubg")
# dell.browsing("edge")

        
    
    






