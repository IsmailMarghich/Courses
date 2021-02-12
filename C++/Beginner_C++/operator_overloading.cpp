#include <iostream>
using namespace std;
//operator overloading is changing how operators work on certain data, this can be on assignments operators
//but also on member functions, global functions and stream insertion (<<)

class MyNumber{ //lets say we have a class that stores data and we want to change its behaviour when we use the assignment operator
public:
    int number; //this is the variable that the class stores, but if we use = between objects, the object will be copied, not the number

    void printnumber(){
        cout << number << endl;
    }//in order to make assigning numbers between objects work, we need to do operator overloading
    void operator=(const MyNumber &rhs){  //return type, operator(operator) (const class data)
        number = rhs.number; //when the = operator is used, this code block will be run, we set number to the number from the right side object
    }
    //we can also overload the << operator to display it more easily
    friend ostream& operator<<(ostream& os, const MyNumber& rhs); //friend the block of code so it can access this class


}; //were returning an ostream, in the code block we add our number variable to the stream
ostream& operator<<(ostream& os, const MyNumber& rhs){
    os << rhs.number;
    return os;
}


int main(){

    MyNumber number1;
    MyNumber number2;
    number1.number = 10;
    number1.printnumber();
    number2 = number1; //assign number 1 variable to number 2
    number2.printnumber();
    //both print 10
    cout << number1 << endl; //we can also just use cout to print the variable, because we overloaded the << operator
}