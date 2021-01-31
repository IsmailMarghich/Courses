#include <iostream>

using namespace std;

int main() {

    int num1; //declare our integer numbers
    int num2;
    int num3;

    cout << "Enter a number: " << endl; //tell the user to enter a number
    cin >> num1; //grab this number with cin and put it in the variable num
    cout << "You entered: " << num1 << endl; //print out the number

    cout << "Enter 2 numbers separated by a space: " << endl;
    cin >> num2 >> num3; //we can ask for multiple variables in one cin, it will search for valid data in your input
    cout << "You entered :" << num2 << " and " << num3 << endl;

    return 0;
}