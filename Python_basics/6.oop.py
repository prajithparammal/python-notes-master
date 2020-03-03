## OOP allows programmers to create their own objects that have methods and attributes.
## Methods acts as a functions that use infromation about the object, as well as the object itself to return results, or change current object.
## OOP allows us to create code that is repeatable and organized.
## Objects are also called classes in python.

class Sample():
    pass
my_sample = Sample()   ## my_sample is the instance of that class
print(type (my_sample))

## Creating attribute:#################################

class Dog():
    def __init__(self,mybreed):  ## Here, breed is an attribute and self is an instance of the object itself.
        self.my_attribute = mybreed

my_dog = Dog (mybreed='Lab')

print (my_dog.my_attribute)

######################################################

class MY_Dog():
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots  ## Expect boolean True/False

my_dog_2 = MY_Dog(breed='lab',name='tommy', spots='False')

print(my_dog_2.breed)
print(my_dog_2.name)
print(my_dog_2.spots)

######################################################
## Class object attributes:

class MY_Dog():
    ## Class object Attribute
    ## Same for any instance of a class
    species = 'mammal'

    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots  ## Expect boolean True/False

my_dog_2 = MY_Dog(breed='lab',name='tommy', spots='False')

print(my_dog_2.breed)
print(my_dog_2.name)
print(my_dog_2.spots)
print(my_dog_2.species)   ## calling class object attribute

######################################################
## Methods are functions defined inside body of the class
## methods should have () while calling them, but attributes dont require it. ie, in below example my_dog_3.bark wont work with  my_dog_3.bark()

class MY_Dog():
    ## Class object Attribute
    ## Same for any instance of a class
    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    ##OPERATIONS/ACTIONS ===> METHODS
    def bark (self):
        print("WOOF!!!!my name is {}".format(self.name))

    def barknum (self, number):
        print("WOOF!!!!my name is {} and the number is {}".format(self.name,number))

my_dog_3 = MY_Dog('labiee','tommyyy')

print(my_dog_3.breed)
print(my_dog_3.name)
my_dog_3.bark()
my_dog_3.barknum(3)

######################################################

class Circle():
    ## Class Object Attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi ## or self.area = radius * radius * Circle.pi

    # Method
    def get_circumfrence(self):
        return self.radius *self.pi * 2

my_circle = Circle(30)
print ("My circle circumfrence is", my_circle.get_circumfrence())
print ("My circle area is", my_circle.area)
######################################################

## Inheritance are way to form new class using class which are already defined.

class Animal():
    def __init__(self):  # init method will automatically executed , when you call animal class
        print("Animal created")
    def who_ami_i(self):
        print ("I am an animal")
    def eat(self):
        print ("I am eating")

class Dog(Animal):  ## Derived class, becoz it is deriving some features of base class Animal
    def __init__(self):
        Animal.__init__(self) ##create an instance of animal class
        print("Dog Created")
    def who_ami_i(self):
        print ("I am an dog")


myanimal = Animal()     ## myanimal is an instance of class
print (myanimal.eat())
print (myanimal.who_ami_i())

my_dog = Dog()
print (my_dog)
print (my_dog.eat())
print (my_dog.who_ami_i())

######################################################
## Polymorphism is different object class can share the same method name.

class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + "says woof!!"


class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + "says meow!!"

niko = Dog ("niko ")
felix = Cat ("felix ")

print (niko.speak())
print (felix.speak())

for pet in [niko,felix]:
    print (type(pet))
    print(type(pet.speak()))

######################################################

def pet_speak(pet):
    print (pet.speak())

pet_speak(niko)
pet_speak(felix)
######################################################

