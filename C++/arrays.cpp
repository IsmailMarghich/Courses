#include <iostream>

using namespace std;

int main() {
    //an array is a sequence of variables where each entry can be accessed by an index, arrays start at 0
    int array[5] = {1, 2, 3, 4,
                    5}; //we define the type of an array, and then in brackets [], we specify how many elements the list has
    // we can then initalize it by putting the values in curly braces {}, separated by comma

    cout << array[0] << endl; //printing first entry
    cout << array[1] << endl; //printing second
    cout << array[-1] << endl;
    //we can make a two dimensional array, by adding another bracket specifying length of dimension
    int twodarray[3][3] = {{1, 2, 3}, //we another set of curly braces for each new column
                           {1, 2, 3},
                           {1, 2, 3}};
    cout << twodarray[1][1]; //accessing second element of second array

    //the issue with arrays is that they are of fixed size, we cant dynamically increase or decrease the size
    //it also doesnt hae a safe guard for out of bound indexes, that is when u use an index that is out of range
    //it also does not work with C++ STL, standard template library, which is a library with lots of handy functions.
    //it is better to use Vectors, which I will cover in vectors.cpp
};