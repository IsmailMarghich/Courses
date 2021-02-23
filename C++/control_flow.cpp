#include <iostream>

using namespace std;

//we can use if, else if and else statements to control the flow of our C++ program
int main() {


    int grade;

    cout << "Enter your grade 1-10: " << endl;
    cin >> grade;
    //we take a grade from the user and see if its good, sufficient or insufficient
    if (grade >= 8) //if its greater or equal to 6 then its sufficient
        cout << "Your grade is good" << endl;
    else if (grade >= 6) //we can check with an if again with an else if statement
        cout << "Your grade is sufficient" << endl;
    else //otherwise, we say its insufficient with the else statement
        cout << "Your grade is insufficient" << endl;

    bool cheated;
    cout << "Did you cheat?, enter a 1 for yes and 0 for no: " << endl;

    cin >> cheated;
    //we can use a nested if statement to check for multiple if's in a row
    if (grade == 10) { //checking if the student got a perfect score
        if (cheated) { //if he cheated we scold him, we can use the boolean as a true or false
            cout << "Dont cheat to get a 10!" << endl;
        } else { //otherwise we give him a complement
            cout << "Wow, you got a 10 without cheating!" << endl;
        }
    }
    int number;

    cout << "Name a number between 1 and 3, and I will tell you what it stands for " << endl;
    cin >> number;
    //since we have multiple different colors as input, instead of if statements, we can use the switch statement
    switch (number) { //we enter a condition in the braces
        case 1:
            cout << "1 is for unity" << endl;
            break; //then we make cases for each value of number
        case 2:
            cout << "2 is for duo's" << endl;
            break;
        case 3:
            cout << "3 is for pyramids and triangles" << endl;
            break;
        default: //we can set a default in case the user enters something we dont have a case for
            cout << "Enter a number between 1 and 3 please" << endl;
            break;
            //we use break after every case so it knows to stop and gets out of the switch
    }

    //we can also use the conditional operator ? for control flow
    bool isUgly;
    cout << "Are you ugly? Enter 1 for yes, 0 for no" << endl;
    cin >> isUgly;
    //condition  expression if true       expression if false
    cout << ((isUgly) ? "No you are not ugly!" : "You are pretty!") << endl;


}