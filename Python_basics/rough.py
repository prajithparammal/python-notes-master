class dog():

    species = 'mammal'
    def __init__(self,breed):
        self.breed = breed

sam = dog(breed='lab')
frank = dog(breed='huskie')

print(sam.breed)
print(frank.breed)
print(sam.species)


class circle():
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * circle.pi

    def setRadius(self, radius):
        self.radius = radius

    def getradius(self):
        return self.radius

c = circle()
c.setRadius(2)
print('radius is :', c.getradius())
print('area is :', c.area())



