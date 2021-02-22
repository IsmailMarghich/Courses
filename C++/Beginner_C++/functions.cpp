#include <iostream>
#include <cmath>
using namespace std;
//we can modularize our program by splitting it into functions
int doublenumber(int number); //we can declare the function here, so we can keep the main function at the top
void printfunction();
void changenumber(int &number);
int defaultfunction(int number = 10);
void printarray(const int numbers [], size_t size);
int recursivefunction(int n);
int main(){

    int n = 16;
    cout << "Our starting number: " << n << endl;

    cout << " Number to the power of two is: " << pow(n, 2) << endl; //power function returns a number to a given power

    cout << "Doubled number: " << doublenumber(n) << endl; //using our double number function

    cout << "Square root: " << sqrt(n) << endl; //the sqrt returns the square root of a given number

    printfunction(); //void means nothing, the function doesnt return anything, nor does it use a parameter, it just prints something

    changenumber(n); //change up the value of variable n

    cout << "The number is now: " << n << endl; //check if variable n is changed
    cout << defaultfunction() << endl; //we pass no argument to this function, the default value is 10, so it returns 10

    int array[5] = {1,2,3,4,5};

    printarray(array, 5); // call function with size of array as well, so the function knows how big the array is

    int fibonacci_number = 10;
    //call our recursive function which call calculate the sum of a fibonacci series until value of n
    cout << "The sum of "<< fibonacci_number << " numbers is: " << recursivefunction(fibonacci_number) << endl;

    return 0;
}

int doublenumber(int number){ //a function that takes an integer parameter called number, and returns an integer
    return number * 2; //returns double of the number passed by parameter
}
void printfunction(){
    cout << "A void function returns nothing" << endl;
}//when you pass an existing variable as argument to a function, it makes a copy
void changenumber(int &number){ //we use & to get to the address of the variable, instead of making a copy, it changes now the actual variable in main
    number = 50; //changes the value of the number
    cout << "Changed number to: " << number << endl;
}
int defaultfunction(int number){
    return number;
}
//with const, we make the array read only, because when u pass an array to a function it uses the actual array, not a copy, so it can be edited
void printarray(const int numbers [], size_t size){
    for (size_t i{0}; i < size; ++i) //for loop to print the whole array, we have to use size_t as its the type for memory sizes in C++
        cout << numbers[i] << endl;
}
int recursivefunction(int n){ //this function will calculate the sum of n amount of numbers in the fibonacci series
    if (n <= 0) //theres no negative numbers in the fibonacci series, so we return zero if we reach zero or negative number
        return 0;
    else if (n == 1) //if we reach the first number, we return 1 since the fibonacci series stars at 1
        return 1;
    return recursivefunction(n-1) + recursivefunction(n-2); //otherwise we call the function to calculate the current and previous value, and add them together
    //the function gets called within the function, this will continue till the base cases are reached, then all the numbers will be summed up together
}