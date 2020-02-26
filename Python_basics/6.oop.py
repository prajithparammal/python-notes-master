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

