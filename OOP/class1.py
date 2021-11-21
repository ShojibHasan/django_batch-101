# class Person:
#     def __init__(self,name,age): #magic method
#         self.name1 = name
#         self.age1 = age
    
#     def address(self):
#         print("I Live in Dhaka")

# person1 = Person("Shojib",24)

# person1.address()


class Calculator:
    def cal1(a,b):
        print(a+b)
        
a = int(input())
b = int(input())
cal = Calculator()
cal.cal1(a,b)