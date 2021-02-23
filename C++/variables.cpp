#include <iostream>

using namespace std;
int globalvar = 5; //we can set global variables outside of a function
//global variables can be accessed from everywhere in the program, unlike local variables
int main() {
    //in C++ we define variables similar to how it is done in C, we specify a type and variable name
    //and then assign a value, if we want to. C++ has lots of different datatype for variables

    int integer = 5; //integers are decimal numbers
    unsigned int positivenumber = 100; //unsigned means this can only store positive values
    short int shortinteger = 1; //short integers can store a shorter range of numbers, which means they take up less memory
    long long int longinteger = 10000000; //we can use long to specify that a datatype has to store higher ranges of values
    //this costs more memory, we can apply to integers and also doubles
    const int constantinteger = 1; //when u use const before initializing a variable, it means it cannot be changed


    float floatingpoint = 10.0; //floating points are numbers decimal point values
    double doublefloat = 10.0; //doubles are like floating point numbers but with a bigger range

    char letter = 'f'; //chars are single letter values
    string stringvar = "A string is an array of characters";

    bool boolean = true; //boolean values can be false and true, we can use them to indicate whether something has to be done
    //with for example a for or while loop

    //all these data types take up a different amount of memory, we can check this with the size_of operator
    cout << sizeof(int) << endl; //integers take up 4 bytes as a minimum
    cout << sizeof(longinteger) << endl; //we can do the same with variables, long long values store take up 8 bytes
    cout << integer << positivenumber << shortinteger << longinteger << endl;

    return 0;
}