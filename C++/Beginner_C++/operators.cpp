#include <iostream>

using namespace std;

int main(){
    int a = 5;
    int b = 10;
    int c {15}; //we can also initialize with brackets

    cout << (b > a) << endl; //comparing with greater or smaller then returns one or zero
    cout << (c >= b) << endl; //we use greater or equal to by adding =

}