#include <iostream>
#include <iomanip>

using namespace std;
//C++ use streams as interface between the program and input and output devices
//a common stream is the ostream and istream, which we can access with cout and cin respectively
int main(){
    int number;

    cout << "Enter a number" << endl;
    cin >> number;
    //we can modify how integers are put in and out of the stream with modifiers
    cout << dec << number << endl; //displays number in decimal format
    cout << hex << number << endl; //displays number in hexadecimal format
    cout << oct << number << endl; //displays number in octadecimal format
    //we can show the bases of these number with showbase modifier
    cout << showbase;
    cout << hex << number << endl; //adds 0x to show base

    float pointnumber;
    cout << "Enter a float: " << endl;
    cin >> pointnumber;
    //float modifiers
    cout << pointnumber << endl; //by default 6 digits is the precision for floating point, this starts from the first digit
    cout << setprecision(9); //change our precision to 9
    cout << pointnumber << endl;
    cout << fixed; //with the fixed modifier, now the precision will start from the first number after the dot, not first digit
    cout << pointnumber << endl;
    cout << showpoint; //with showpoint modifier, it will add trailing zeroes to missing numbers until precision limit
    cout << pointnumber << endl;


}