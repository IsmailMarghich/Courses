#Given the below class:
# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def oldestcat(*args):  #Create a function that finds the oldest cat
        return max(args)

tom = Cat('tom', 10)  #Instantiate the Cat object with 3 cats
bob = Cat('bob', 12)
jake = Cat('jake', 17)
print('The oldest cat is', Cat.oldestcat(tom.age, bob.age, jake.age),'years old.')
# Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
