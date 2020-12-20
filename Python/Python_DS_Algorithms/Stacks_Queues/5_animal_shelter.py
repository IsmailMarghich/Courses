# Imagine an animal shelter which operates with a 'first in, first out' basis, meaning people must choose the oldest animal.
# In this scenario we will have two animal types, Cats and Dogs, Cats have the priority in this scenario, meaning those will get adopted first
# Create a datastructure which simulates this scenario with operations such as enqueue, dequeue, dequeueDog and dequeueCat
class AnimalShelter():
  def __init__(self):
    self.cats = []
    self.dogs = []

  def enqueue(self, animal, type): #enqueing to which type list
    if type == 'Cat':
      self.cats.append(animal)
    else:
      self.dogs.append(animal)

  def dequeueCat(self): #remove something from cat list
    if len(self.cats) == 0:
      return None
    else:
      cat = self.cats.pop(0)
      return cat

  def dequeueDog(self): #remove something from dog list
    if len(self.dogs) == 0:
      return None
    else:
      dog = self.dogs.pop(0)
      return dog

  def dequeueAny(self): # remove cat first but if there are no cats, remove a dog instead
    if len(self.cats) == 0:
      result = self.dogs.pop(0)
    else:
      result = self.cats.pop(0)
    return result


customQueue = AnimalShelter()
customQueue.enqueue('Cat1', 'Cat')
customQueue.enqueue('Cat2', 'Cat')
customQueue.enqueue('Dog1', 'Dog')
customQueue.enqueue('Cat3', 'Cat')
customQueue.enqueue('Dog2', 'Dog')
print(customQueue.dequeueDog())
print(customQueue.dequeueDog())

print(customQueue.dequeueAny())
