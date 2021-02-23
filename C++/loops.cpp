#include <iostream>

using namespace std;
//if we wanna repeatably run pieces of code, we can use looping

int main() {
    //a for loop consists of 3 parts
    //initialization condition increment
    for (int i = 1; i <= 5; i++) //this will run the code in the loop, until i is not less than 6 anymore
        cout << "Loop: " << i << endl; //each iteration, i will increase by 1

    //there is also a newer for loop, introduced in C++ 11, it is called the range based for loop
    int array[] = {1, 2, 3, 4, 5};
    int sum = 0;
    // (type)variable collection to iterate over
    for (int number: array) {
        cout << number << endl; //this will print each item in the array
        sum += number; //each iteration, we add the number to the sum
    }
    cout << "Sum: " << sum << endl;

    int condition = 1;
    //there is also a while loop, where code gets repeated until a single expression becomes false
    //this is checked before executing the code the first time, unlike the for loop
    while (condition <= 5) {
        cout << condition << endl; //print our number everytime
        ++condition; //increment it, after 5 iterations, the loop stops
    }
    //we can also use the while statement to repeatedly check user input
    int num = 0;
    while (num <= 100) { //this loop will ask the user for a number until the number given is above 100
        cout << "Enter a number above 100: " << endl;
        cin >> num;
    }
    //there is also a different type of while statement, a do while statement.
    //it is similar to a while statement, but the block of code is executed before the condition is executed
    int input = 200;

    do { //do this block of code, as long as condition under the block is satisfied
        cout << "Enter a number under 100: " << endl;
        cin >> input;
    } while (input > 100);

    //we can control loops from inside the code block as well, with the continue keyword, the loop will stop its iteration and start the next one
    //with the break keyword, we can stop the keyword
    string answer = "continue";

    while (answer == "continue") {
        cout << "Do you want to continue or break?: " << endl;
        cin >> answer;
        if (answer == "break")
            break;
        else
            continue;
        cout << "This code wont run because of the continue statement, which starts the next loop";
    }
    cout << "The loop broke, now the code under it gets run" << endl;

}