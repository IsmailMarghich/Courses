#include <iostream>
#include <cmath>
//inheritance allows us to make classes out of existing classes that will inherit its variables and methods
//this means we have to write less code because we re use classes
using namespace std;
class Account{ //We have a base class for an account at a bank
public:
    int balance = 0; //variable for balance

    void deposit(int amount){ //deposit and withdraw functions to remove and add money
        balance += amount;
        cout << "Deposit " << amount << "$" << endl;
    }
    void withdraw(int amount){
        balance -= amount;
        cout << "Withdraw " << amount << "$" << endl;
    }
    Account(int amount){ //constructor to start with an amount
        balance = amount;
    }
    Account() {} //default constructor
};
class Savings_Account: public Account{ //we create a sub class of Account class, now it will get its variables and methods
private:
    float interest_rate; //this sub class adds an interest rate variable
public:
    void calculate_interest(int years){ //function to calculate how much interest you will be gaining on your savings account
        double gained = (balance * pow(((interest_rate / 100) + 1), years)-balance); //this calculates the amount of money gained based on interest rate, given years
        cout << "You earned " << gained << " on " << balance << "$" << endl; //print out how much is gained
    }
    Savings_Account(int amount, float interest){ //constructor to start an account, u can fill in starting balance and your interest rate
        balance = amount;
        interest_rate = interest;
    }
    Savings_Account(){ //we can also use the parent class constructors in the child class constructor
        Account(), interest_rate = 0; //we make a basic account class, and set interest rate to 0 for default constructor
    }
    Savings_Account(int amount){ //constructor when user only enters amount of money
        (Account(amount)), interest_rate = 0; //we make use of our parent class constructor
    }
};
//we can also change up the functions inherited by a class
class Tax_Account: public Account{ //gets variables and methods from Account clqss
public:
    void deposit(int amount){ //we write the same function prototype
        amount = amount - (amount / 100) * 3; //we add modification, this removes 3% from the amount
        Account::deposit(amount); //we call the same function
    }

};
int main(){
    Savings_Account bob{1000, 5}; //we make a savings account class
    bob.withdraw(500); //as you can see, the parent Account class methods work on the sub class
    bob.deposit(500);
    bob.calculate_interest(5); //we can also use the new functionality added in the subclass

    Savings_Account beb;
    cout << beb.balance << endl;

    Savings_Account james{100};
    cout << james.balance << endl;

    Tax_Account jeremy;
    jeremy.deposit(100); //we deposit 100 in tax account
    cout << jeremy.balance << endl; //prints 97 because we removed 3%
}