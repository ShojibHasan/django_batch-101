class Person:
    def __init__(self,name,age):
        self.name=name
        self.age = age
        print(self.name,self.age)
    def address(self):
        print("Dhaka")

# class Office(Office):
#     def office_address(self):
#         print("Baridaha J Block", self.name)
class Office():
    def office_address(self):
        print("Baridara")

class MyHome(Person,Office):
    def home_number(self):
        print("016987687")
    


offi = MyHome("Shojib","24")
offi.home_number()
offi.office_address()


# myhome = MyHome("Hasan","1321231")
# myhome.home_number()
# class Student(models.Model):
#     name = model.Char("")