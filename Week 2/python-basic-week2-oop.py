#Class declaration
class Bird:
    #Class attribute, it's same for every object.Can also be called from class
    wings = 2
    #Any method with 2 underscore on both side is a magic method 
    #Constructor, every class have this method and it's automatically called every time a object is instanciate
    def __init__(self,type,color):
        #These are object attributes
        self.type = type
        self.color = color
    
    #A method in class
    def fly(self,distance):
        print(f'{self.type} can fly {distance} Kilometers')

    #Class method, this method doesn't need self. It can be called directly by class. it's first argument is the class itself and it return a class object
    @classmethod
    def new_bird(cls, type):
        return cls(type,type)
    
    #Static method, this method is exactly like class method but don't require class object
    @staticmethod
    def has_eaten(amount):
        print('this bird needs ' + amount + 'kg of food')

    #property is type of variable that can be protected. if we want to set the value of a property attribute, the setter method is called and if we want to see
    #the value the getter method is called
    @property
    def can_be_eaten(self):
        return False


#Inheritance, here SmallBird is subclass and Bird is superclass
class SmallBird(Bird):
    #This method has overwritten the the method from superclass
    def fly(self,distance):
        #super() is used to access any attribute or method from the super class
        print(f'{self.type} can fly {distance} Meters and it has ' + str(super().wings) + ' wings')

a = Bird('Pigeon', 'White')
b = SmallBird('Dove', 'Ash')
c = Bird.new_bird('Crow')

print(f'This is a {a.type}, it\'s color is {a.color}')
a.fly('50')
print(f'This is a {b.type}, it\'s color is {b.color}')
b.fly('30')
print(f'This is a {c.type}, it\'s color is {c.color}')
c.fly('65')
print(f'Every Bird has {Bird.wings} wings') #this can also be accessed by a.wings, b.wings, c.wings
print(SmallBird.has_eaten('1.5'))

print(str(a.can_be_eaten))

"""
Object Life Cycle
1)Creation: When a class is created (not object)
2)Manipulation: When an object is initialized
3)Destruction: After useage (code done executed) the object is destroyed
"""

"""
Automatic Memory Management
Reference Count is the number of variable, object or attribute an object refers to (or connected to). If the reference count of an object becomes 0, then python
automatically destroys that object. This is called Automatic Memory Management
"""

"""
Weakly Private
There is no private/protected variable in python. But using underscore before a variable (_fp) hints that this variable shouldn't be accessed without creating an
object. These underscored variables will also not be imported.
"""

"""
Strongly Private
Using double underscore before a variable makes it not accessable without a method
"""