# Parent class / Base class / Super class
# Child class / Derived class / Sub class

# 1. SINGLE INHERITANCE
# A child class inherits from a parent class
"""
print("\n1. SINGLE INHERITANCE\n")

class Father:
    precious_thing = 'gold watch'

class Son(Father):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def disp(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f"Inherited from Father: {self.precious_thing}")

beta = Son("Ramesh", 20)
beta.disp()
"""

# 2. MULTIPLE INHERITANCE
# A child class inherits from multiple parent classes

""" 
What happens when there is a variable in all three classes(Father, Mother and Son) with the same name(i.e precious_thing)? How to solve this name ambiguity problem?

# 1. use parent name to access the parent class variables (as done below)
# 2. use super() to access immediate parent class attributes in the MRO (method resolution order)
"""

"""
print("\n2. MULTIPLE INHERITANCE\n")

class Father:
    precious_thing = 'gold watch'

class Mother:
    precious_thing = 'diamond ring'

    def display_it(self):
        print(f'Accessing Father\'s precious thing from Mother class using super(): {super().precious_thing}')

class Son(Mother, Father):
    precious_thing = 'pen'
    def __init__(self, name, age):        
        self.name = name
        self.age = age
    
    def disp(self):
        print(f'Son\'s Name: {self.name}')
        print(f'Son\'s Age: {self.age}')
        # print(f"Son Inherited from father: {self.precious_thing}") # output: Son Inherited from father: pen
        # print(f"Son Inherited from mother: {self.precious_thing}") # output: Son Inherited from mother: pen

        # since both parent class have same variable name, so we can't use super() to access them, therefore ClassName is used
        print(f"Son Inherited from father: {Father.precious_thing}")
        print(f"Son Inherited from mother: {Mother.precious_thing}")
        super().display_it() # super() accesses immediate parent's (i.e Mother's) attributes in MRO


beta = Son("Suresh", 20)
beta.disp()
print(Son.__mro__) # output: (<class '__main__.Son'>, <class '__main__.Mother'>, <class '__main__.Father'>, <class 'object'>)

# Q. There is no inheritance between Father and Mother class even then the display_it() of mother class is able to access the variable of father class, how?

# - When super() is called in Mother, it looks up the next class in the MRO, which is Father. Therefore, super().precious_thing in the Mother class accesses the precious_thing attribute from the Father class, not because there is a direct inheritance relationship between Father and Mother, but because Father is next in the MRO for the Son class.
"""

# 3. HIERARCHICAL INHERITANCE
# many classes inherit from a single parent class
"""
print("\n3. HIERARCHICAL INHERITANCE\n")

class Father:
    precious_thing = 'gold watch'

class Son(Father):
    def __init__(self, name):
        self.name = name
    
    def disp(self):
        print(f'Name: {self.name}')
        print(f"Inherited from father: {Father.precious_thing}")

class Daughter(Father):
    def __init__(self, name):
        self.name = name
    
    def disp(self):
        print(f'Name: {self.name}')
        print(f"Inherited from father: {Father.precious_thing}")

beta = Son("Raja")
beta.disp()
beti = Daughter("Pari")
beti.disp()
"""

# 4. MULTI-LEVEL INHERITANCE
# A class inherits from a parent class which itself is inheriting from another class
# or A subclass inherits from another subclass.

"""
print("\n4. MULTI-LEVEL INHERITANCE\n")

class Grandparent:
    precious_thing = 'gold watch'

    def display_precious_thing(self):
        print(f'Grandparent\'s precious thing: {self.precious_thing}')


class Parent(Grandparent):
    precious_thing = 'diamond ring'

    def display_it(self):
        # Call the Grandparent's display_precious_thing method
        super().display_precious_thing()
        print(f'Parent\'s precious thing: {self.precious_thing}')


class Child(Parent):
    precious_thing = 'pen'

    def __init__(self, name, age):
        super().display_it()  # Calls the Parent's display_it method
        self.name = name
        self.age = age

    def disp(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f"{self.name} Inherited from grandparent: {Grandparent.precious_thing}")
        print(f"{self.name} Inherited from parent: {Parent.precious_thing}")


# Creating an instance of Child
beta = Child("Suresh", 20)
beta.disp()
"""

# 5. HYBRID INHERITANCE
# A combination of two or more types of inheritance.
# """
print("\n5. HYBRID INHERITANCE\n")

class Grandparent:
    gp_precious_thing = 'antique sword'

class Father(Grandparent): # single inheritance
    def display_it(self):
        print(f'Father inherited from Grandparent: {self.gp_precious_thing}')


class Mother:
    precious_thing = 'gold watch'
    def display_it(self):
        print(f'Mother\'s precious thing: {self.precious_thing}')


class Son(Mother, Father): # multiple inheritance
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def disp(self):
        super().display_it()  # This will call Mother's display_it() method due to MRO
        Father.display_it(self)  # Explicitly call Father's display_it() method
        print(f'Son\'s Name: {self.name}')
        print(f'Son\'s Age: {self.age}')
        print(f"Son inherited: {self.precious_thing} from Mother and {self.gp_precious_thing} from Grandparent through Father")

# Creating an instance of Son
beta = Son("Suresh", 20)
beta.disp()
# """