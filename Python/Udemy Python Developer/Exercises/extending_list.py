#Create a class that changes up the len() function to return 1000
class SuperList(list): #our class that is a subclass of list
    def __len__(self): #len function
        return 1000 #replace it with return 1000

super_list1 = SuperList() #instance of the class

print(len(super_list1)) #print the modified len function
super_list1.append(5) #append to show its a list
print(super_list1[0]) #print what u append, to show its a list
