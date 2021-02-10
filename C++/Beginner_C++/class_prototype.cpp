#include <iostream>

using namespace std;

//we can also define class methods outside of the class, we do have to have a prototype in te function howver
class Account {
private:
    double balance;
public:
    void set_balance(double bal); //we prototype our functions which we declare later

    double get_balance();
};

void Account::set_balance(double bal) { //implementation of our functions
    balance = bal;
    cout << "I set the balance to: " << balance << endl;
}
 //the :: is the scope resolution operator, we tell C++ to specifically go into that class for that method
 //we have to do this because the implementation of the method isn't in the class just the prototype
double Account::get_balance() {
    return balance;
}

int main() {

    Account myaccount; //make an instance of Account class
    myaccount.set_balance(1000); //set balance
    cout << myaccount.get_balance() << endl; //get balance
    //this way, we can clean up the class, especially if we have large methods we can abstract away
    //you will also notice that even if the functions are implemented somewhere else, it can still access private parts of the class
}