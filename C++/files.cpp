#include <iostream>

using namespace std;
//to read and edit files we use the file streams in C++
#include <fstream>

int main() {
    //lets first read from a file, which says Hello, and has a number 100 in it
    fstream input_file; //declare a stream
    string line; //declare a string where we can put our read text
    int number; //an int to store the number in

    input_file.open("text.txt"); //open our text file
    if (!input_file) {  //if text file isnt there, error
        cerr << "Could not open file";
        return -1;
    }
    cout << "File is good to go" << endl;
    input_file >> line >> number; //because a file is a stream, we can simply put the file in variables with >> operator
    cout << line << endl; //print Hello
    cout << number << endl; //print 100

    //now lets write to a file
    ofstream output_file{"output.txt"}; //create an ofstream object, we name it output.txt
    string input;

    if (!output_file) {
        cerr << "Error creating file" << endl;
        return -1;
    }
    cout << "File has been created" << endl;

    cout << "Enter something to write to the file: ";
    getline(cin, input); //we need to use getline, because we are using string objects, not C style strings for input
    output_file << input << endl; //put our text into the output file

    output_file.close();
}