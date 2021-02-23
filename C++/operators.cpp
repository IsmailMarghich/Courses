#include <iostream>

using namespace std;

int main() {
    int a = 5;
    int b = 10;
    int c{15}; //we can also initialize with brackets

    cout << (b > a) << endl; //comparing with greater or smaller then returns one or zero
    cout << (c >= b) << endl; //we use greater or equal to by adding =

    a--; //we can increment and decrement a value by 1 with ++ and  --
    b++;
    cout << a << endl;
    cout << b << endl;

    a += a; // += is assigning and adding at the same time: a = a + a
    cout << a << endl;

    a = 5;
    b = 10;
    double average = (a + b) / 2; //we use a double here because we want to see decimals
    cout << average << endl; //should print 7.5, but it does not. the numbers are integers
    //we can 'cast' an expression to a certain type, this means it C++ will convert or keep that expression that datatype
    average =
            static_cast<double> (a + b) / 2; //we cast the expression to a double, now it will have numbers after period
    cout << average << endl; //now it will print 7.5

    bool positive = true;
    bool negative = false;
    //&& (and) ! (not) and || (or) are logical operators which evaluate to true or false
    cout << (positive && positive) << endl; // && returns true if both operands are true
    cout << !(positive && positive)
         << endl; // ! returns the opposite value, so true becomes false, and false becomes true
    cout << (positive || negative) << endl; //returns true if either of the operands is true
}