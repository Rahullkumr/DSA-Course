class Student:
    std = 9
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f'Name: {self.name} and age: {self.age}')
        print("Studies in class: ", self.std)

s1 = Student("Rahul", 13)
s1.display()
s1.name = "Prince"
s1.age = 10
s1.std = 7
s1.display()
