#include <iostream>
#include <vector>
#include <memory>
using namespace std;
//smart pointers are pointers which manage their own memory, and come with extra features compared to C pointers
class Account { //A basic class to use as example for smart pointers
public:
    int balance = 0;

    void display(){
        cout << "Balance: " << balance << endl;
    }

    Account(int amount){
        balance = amount;
    }
};
int main () {
    { //create a specific code block for the smart pointer
        //only one unique pointer can point to the same object, this is handy to prevent 2 pointers pointing to the same thing
        unique_ptr<int> p1{new int{100}}; //we need to initialize the pointer based on a template, this case an integer
        //we can immediately assign value to the pointer
        cout << *p1 << endl;
        //we can also initialize unique pointers with make_unique function
        unique_ptr<int> p2 = make_unique<int>(
                200); //make unique will return a unique pointer based on the template and value given
        cout << *p2 << endl; //this is faster because we dont use new or delete keyword
    } //at the end, the smart pointer will clean itself up

    //we can use smart pointers to point to classes
    unique_ptr<Account> cpointer1{new Account{100}};
    cpointer1->display(); //we can use class variables and methods with the -> operator, just like normal pointers
    unique_ptr<Account> cpointer2 = make_unique<Account>(200);
    cpointer2->display();

    //we can also move smart pointers around with move keyword
    unique_ptr<Account> cpointer3;
    cpointer3 = move(cpointer1); //now cpointer 3 will refer to cpointer 1, while cpointer 1 will become a null pointer
    cpointer2->display(); //will print out cpointer 1's previous value

    vector<unique_ptr<Account>> accounts; //we can put smart pointers in vectors too
    accounts.push_back(make_unique<Account>(100));
    accounts.push_back(make_unique<Account>(200));
    accounts.push_back(make_unique<Account>(300));

    for (const auto &acc: accounts) //for loop that print each class their balance, we have to dereference with & because they are pointers
        cout << acc->balance << endl;
    //notice how we never have to delete or set pointers to NULL, smart pointers automatically manage their memory

    //shared pointers can point to the same object and allows for assigning
    shared_ptr<Account> p1 = make_shared<Account>(1000); //shared pointer for an object with value 1000
    shared_ptr<Account> p2 = p1; //assign p1 to p2
    p1->display(); //both print 1000
    p2->display();
    cout << p1.use_count() << endl; //with use_count method, we can see how many shared pointers point to the same object

    return 0;
}