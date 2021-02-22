#include <iostream>
//C++ is a language based on C, in the beginning it was called it was called C with classes because it added classes
//Classes a collection of data used to store variables and methods of a certain class, we can have instances of a class that we call objects
//An std array or vector variable is an instance of a class, in this class we can find the methods associated with that class
//An example of this would be the .size method for a vector, with classes we can have methods specific to objects and classes
//Where as in C we have to use functions for everything since there is no classes in C
using namespace std;

//lets say we want to store data about lots of different cars, we can use a class for this
class car {

public: //public access modifier, it means all the variables and data in this block will be accessible by the rest of the program
    string name; ///4 different variables specific to the car class
    int age{};
    bool checked{};
    int price{};

    void printdata() const { //we add a method that prints the data that the car holds
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Checked: " << checked << endl;
        cout << "Price: " << price << endl;
    }

private:
    string name; //everything in the private section of a class can only be accessed by the same objects or objects who are 'friends with this class'
};

int main() {
    //we make sure our class definition is outside of main, so any function in the program can use it

    car mycar; //we can now make an instance of our car classes, called 'mycar'
    mycar.name = "Toyata"; //we can use the . and the variable name to change the value of the variable
    mycar.age = 27;
    mycar.checked = true;
    mycar.price = 10000;
    mycar.printdata(); //we can use the printdata method on our instance of car class
    //our main function is much more compact now, the car class and its variables & functions are now abstracted away
}