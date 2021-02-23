#include <iostream>
//Dynamic Polymorphism allows us to change how inheritance works with classes
using namespace std;
//lets say we have 2 classes with a function with the same name

class Base {
public:
    virtual void say_hello() const { //remove virtual keyword at first
        cout << "Hello I am a base class" << endl;
    }

};

class Derived : public Base {
public:
    virtual void say_hello() const { //remove virtual keyword at first
        cout << "Hello I am a derived class" << endl;
    }

};

void say_hello_poly(
        const Base &obj) { //hello function that will use the say hello method of a Base class or derivative of Base class
    cout << "Hello:";
    obj.say_hello();
}

void dynamic_function(Base &ref) {
    ref.say_hello();
}

int main() {
    Base a; //calls base function
    a.say_hello();
    Derived b; //this will call its own function
    b.say_hello();

    Base *ptr = new Derived; //a pointer of type Base class, that points to a Derived class
    ptr->say_hello(); //this prints out the based class method, because C++ decides which function to use at compile time
    //and at compile time, the compiler sees in the function that it uses a Base class, so it uses that, but it should use a different method
    //we can solve this with virtual functions
    //if a function is virtual it will be decided in runtime to which object it belongs, now the say hello function says
    //its from the derived function, rather than the base function

    //we have use base class references as references to objects
    Base c;
    Base &cref = c; //cref is a reference to object C
    cref.say_hello(); //we can use cref to access the object
    dynamic_function(cref); //this function works with references to classes, rather than using the object itself
}