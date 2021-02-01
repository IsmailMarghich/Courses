#include <iostream>
#include <vector>

using namespace std;

int main(){
    //vectors can dynamically decrease and increase, and support more functions and STL than the default C arrays
    vector <int> numbervector = {1,2,3,4,5};

    cout << numbervector[0] << endl; //printing first entry
    //because vectors are objects, they have methods, these are functions specific to vectors

    numbervector.at(0) = -1; //we can access the vector entries with .at method, the .at method does return an error when it is out of bound
    numbervector.push_back(6); //with push back we can add another element to vector, automatically assigns the memory
    cout << numbervector[0] << endl; //we can see our first entry is changed
    cout << numbervector[5] << endl; //we have a new 6th entry in our vector
    //we can use .size() method to return the size of vector
    cout << "There are " << numbervector.size() << " Elements in the vector" << endl;

}