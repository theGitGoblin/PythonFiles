class Pet:
     def  __init__(self, name, age):
        self.name = name
        self.age = age
     def show(self):
         print(f"I am {self.name}, and I am {self.age} years old")
        

class Cat(Pet):
    def Speak(self):
        return "Meow"


class Dog(Pet):
    def Speak(self):
        return "Woof"
    
p = Pet("tim", 13)
p.show()

cat = Cat("Man", 2)
cat.show()