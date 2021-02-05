#include <iostream>
#include <string> //standard C++ string library
using namespace std;

int main(){

    string s1 = "Frank";
    string s2 = {s1, 0, 3}; //within the curly braces, we can decide what characters are initialized into the string

    cout << s2 << endl; //prints first to third letter

    //we can concatenate 2 strings together
    cout << s1 << " -> " << s2 << endl;

    //under the hood, strings are arrays of characters
    for (int c: s1) //when we change characters to integers, they become the ascii number
        cout << c << endl;

    cout << s1.substr(0, 4) << endl; //we can use the subtr method to get a certain range of characters from a string
    //prints Fran

    cout << s1.find('a') << endl; //the find method will search specific character or string and returns index
    //Prints 2 because a is located at index 2

    cout << s1.length() << endl; // length method returns length of string

    //the cin function only reads strings until first space, so only single words are read
    string line;
    //we can use getline function to read a whole line into a string
    cout << "Enter a string with lots of spaces: " << endl;
    getline(cin, line);

    cout << line << endl;


}