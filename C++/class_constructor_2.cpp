#include <iostream>
using namespace std;
//continuation of class constructor 1
//we will implement, constructor initialization lists, delegate constructors and copy constructors

class Player {
public:
    string name{};
    int health{};
    int xp{};

    //we can construct in a more efficient way with constructor initialization lists
    Player(string name_val, int health_val, int xp_val) //we prototype our constructor, then after a colon we initialize the fields, separated by commas
    : name(name_val), health(health_val), xp(xp_val){} //this way, we can immediately initialize class variables when we get them
    //as opposed to waiting for the constructor to assign them. If we did not do this, the fields would need to be made empty again to assign values

    //with delegate constructors, we can delegate constructors to a constructor initialization list, so we dont have to write lots of code
    Player(){ //no arg constructor
        Player("None", 0 , 0); //now we call the 3 argument constructor, and pass our none values to it
    }   //this saves us writing, and makes the code cleaner, Dont Repeat Yourself

    //a copy constructor will construct an object, based on another object, however C++ uses a copy of an object when it references it
    //so we have to go to the source of the object to change the values/
    Player(const Player &source)
    : name(source.name), health(source.health), xp(source.xp){
        cout << "Successfully copied from: " << source.name << endl;
    };

};


int main(){

    Player james{"james", 100, 200}; //make object with initialization lists
    cout << james.name << endl;
    Player copyofjames {james}; //make a copy of the james object with a copy constructor
    cout << copyofjames.name << endl;
}