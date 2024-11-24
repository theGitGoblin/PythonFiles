class Pet:
     def  __init__(self, name, age):
        self.name = name
        self.age = age
     def show(self):
         print(f"I am {self.name}, and I am {self.age} years old")
        

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def Speak(self):
        return "Meow"
    def say_Color(self):
        print(self.color)
        return 

class Dog(Pet):
    def Speak(self):
        return "Woof"
    
p = Pet("tim", 13)
p.show()

cat = Cat("Man", 2, "red")
cat.show()
cat.say_Color()

d = Dog("iggy", 10)

d.show()