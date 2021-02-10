#include <iostream>
//Constructors and destructors can be used to specify how an object is initialized and de initialized
using namespace std;
//lets make a class for a player in a videogame
class Player{
public:
    string name{};
    int health{};
    int xp{};

    Player(){}; //we can specify how this class can be constructed by setting what arguments u can use
    Player(string name){};
    Player(string name, int health, int xp){};
    ~Player(){}; //this is our destructor, when the objects are out of scope and not on the stack anymore
    //they will get deleted, and the memory will be freed up, this can prevent errors and bugs
    //we can edit these constructors, they work like functions
    Player(string name, int xp){
        cout << "You forgot to set health!" << endl;
    }
    //when we only use 2 arguments, this constructor is called and it will sent a message, we can do all sorts of things in constructors
};
int main(){
    //method 1, Player();
    Player bob;
    bob.name = "Bob";
    bob.health = 100;
    bob.xp = 10000;
    //method 2 Player(string name);
    Player kevin{"Kevin"};
    //method 3  Player(string name, int health, int xp);
    Player erwin{"Erwin", 200, 20000};

    Player nohealth{"Nohealth", 200};
}