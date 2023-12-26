"""Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects."""

# class Myclass:
#   x=5
# print(Myclass)
# p1 = Myclass
# print(p1.x)


class Car:
   number_of_wheels = 4
     #class variable
   def __init__(self,make,model,year):
      #instance variables
      self.make = make
      self.model = model
      self.year = year
  

   def start(self):
    print("The {} {} is staring".format(self.make,self.model))

my_car = Car("volvo","benze",1190)

my_car.start()