#include <iostream>

using namespace std;

double exception_function(int sum, int total);

int main() {
    double average;
    int sum;
    int total;

    cout << "Enter sum: " << endl;
    cin >> sum;
    cout << "Enter total: " << endl;
    cin >> total;

    try {
        if (total == 0) //we cant divide by zero
            throw 0; //we throw an exception if total is 0
        if (total < 0 || sum < 0)
            throw string("Negative value error");
        average = sum / total; //this code will not get run if the exception is called
        cout << "No errors detected.. Continue program" << endl;
        cout << "Average: " << average << endl;
    }
    catch (int &ex) { //we throw a zero if total == 0, we use an integer catch to catch it
        cerr << "Cant divide by zero" << endl; //we catch the exception and use cerr to print an error message
    }
    catch (string &ex) { //if either variables are negative, we throw a string that we catch here
        cerr << ex << endl; //ex is the exeptation that is thrown, this will error out "Negative value error"
    }
    double avrg = exception_function(10,
                                     2); //change the second argument to zero, to see a different way of exception handling
    cout << "Average: " << avrg << endl;
}

//we can also catch exceptions with functions
double exception_function(int sum, int total) {
    if (total == 0)
        throw runtime_error(
                "Cannot divide by zero, please enter a total above 0"); //we can also use throw to handle exceptions
    return static_cast<double>(sum) /
           total;                                         //this is however limited, because we need to use if statements
}