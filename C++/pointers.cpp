#include <iostream>

using namespace std;

//pointers are special type of variables which hold the memory addresses of another variable
int main() {

    int number = 10; //number variable
    int *pointer = NULL; //we make our pointer variable of type int, and set it to nothing

    pointer = &number; //we set the pointer to the address of number with the & symbol, now the pointer contains the address of the number

    cout << "Value: " << *pointer
         << endl; //we dereference the pointer by using the *, now it will go to that memory address and grab the variable
    cout << "Address of pointer: " << &pointer << endl; //with & we access the memory address of a variable
    cout << "Address of value (what a pointer stores): " << &number << endl;

    //C++ added smart pointers, which are an improvement to the old C pointers
    //because of this, I will not go into depth with the C pointers, check out my C folders for that
    //I will continue with pointers in the smart pointer section of this course

    return 0;
}