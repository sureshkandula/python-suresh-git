'''
class Sample():
    pass
# Instance of Sample
x = Sample()

print(type(x))

class Suresh():
    pass
y=Suresh()
print(id(y))

class shruthika():
    pass

z=shruthika()

print(id(z))

var1 = [1,2,3]

a = var1.count(2)
print(a)

print(type(a))
print(type([]))
print(type(()))
print(type({}))

print("###################")
print("#  Objects")
print("###################")

# use type() to check the type of object something is:

# So we know all these things are objects, so how can we create our own Object
#  types? That is where the *class* keyword comes in.

print("###################")
print("# Class")
print("###################")

# The user defined objects are created using the class keyword. The class is a
# blueprint that defines a nature of a future object. From classes we can
# construct instances. An instance is a specific object created from a particular
# class.

# For example, above we created the object 'a' which was an instance of a list object.
#
# Let see how we can use **class**:

# Create a new object type called Sample
class Sample():
    pass

# Instance of Sample
x = Sample()

print(type(x))
# By convention we give classes a name that starts with a capital letter.
# Note how x is now the reference to our new instance of a Sample class.
# In other words, we **instantiate** the Sample class.
#
# Inside of the class we currently just have pass.
#  But we can define class attributes and methods.
#
# An **attribute** is a characteristic of an object.
# A **method** is an operation we can perform with the object.
#
# For example we can create a class called Dog. An attribute of a dog may be its
# breed or its name, while a method of a dog may be defined by a .bark() method
# which returns a sound.
#
# Let's get a better understanding of attributes through an example.
#
print("###################")
print("# Attributes")
print("###################")

# The syntax for creating an attribute is:
#
#     self.attribute = something
#
# There is a special method called:
#
#     __init__()
#
# This method is used to initialize the attributes of an object. For example:

class Dog():
    def __init__(self,breed):
        self.breed = breed

sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')

print(sam.breed)
print(frank.breed)

class Flat():
    def __init__(self,type):
        self.type = type
choice1=Flat(type='2bhk')
choice2=Flat(type='3bhk')

print('choice1:' ,choice1.type)
print('choice2:',choice2.type)

class School():
    def __init__(self,medium):
        self.medium=medium
meridian=School(medium='English')
dav=School(medium='Hindi')

print('meridian :',meridian.medium)
print('dav :',dav.medium)

print ('**************')

class Dog():
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = Dog('Lab','doberman')

print(sam.breed)
print(sam.name)

# Note that the Class Object Attribute is defined outside of any methods in the
# class. Also by convention, we place them first before the init.

print(sam.species)

print("###################")
print("# Methods")
print("###################")

# Methods are functions defined inside the body of a class. They are used to
# perform operations with the attributes of our objects. Methods are essential
# in encapsulation concept of the OOP paradigm. This is essential in dividing
# responsibilities in programming, especially in large applications.
#
# You can basically think of methods as functions acting on an Object that take
# the Object itself into account through its *self* argument.
#
# Lets go through an example of creating a Circle class:

class Circle():
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius

    def area(self):
        return self.radius*self.radius*Circle.pi
    def setRadius(self,radius):
        self.radius=radius
    def getRadius(self):
        return self.radius
c=Circle()
c.setRadius(2)
print('Radius i:', c.getRadius())
print('Area is:', c.area())

# Great! Notice how we used self. notation to reference attributes of the class
# within the method calls. Review how the code above works and try creating your own method
#

print("###################")
print("# Inheritance")
print("###################")

# Inheritance is a way to form new classes using classes that have already
# been defined. The newly formed classes are called derived classes, the classes
# that we derive from are called base classes. Important benefits of inheritance
# are code reuse and reduction of complexity of a program. The derived classes
# (descendants) override or extend the functionality of base classes (ancestors).
#
# Lets see an example by incorporating our previous work on the Dog class:

class Animal():
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()
d.whoAmI()
d.eat()
d.bark()

##############################function revision###############################################
def function(mylist1):
    mylist1=([4,5,6])
    print('see here:', mylist1)
    return

mlist =([1,2,3])
function(mlist)
print('see;', mlist)

def mul(arg1,arg2):
    total= arg1*arg2
    print('see here arthimatic:', total)
    return total
suresh =mul(7,8)
print('see suresh;', suresh)

##################################end####################################################################

def centos(gunnu11):
    gunnu11.append([1,2,3,4])
    print('see here apendone:', gunnu11)
    return
mlist =[5,6,7,8]
centos(mlist)
print('see;', mlist)

#####################################################################################################
'''
class Animal():
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()
d.whoAmI()
d.eat()
d.bark()
