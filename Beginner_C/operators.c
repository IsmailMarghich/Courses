#include <stdio.h>

int main() {
    int a = 10;
    int b = 5;
    //arithmetic operators are mathemical functions that take two operands and perform calculations on them
    a + b;
    a - b;
    a * b;
    a / b;
    a % b; // returns the reminder of integer division
    a++;  //increases by 1
    a--; //decreases by 1

    // logical operators
    a && b; //AND operator, returns true if both are true
    a || b; //OR operator, returns true if a or b are true
    !(a && b); //NOT operator, returns the opposite of the expression after it

    //assignment operators
    a = b;
    a += b; //a is equal to a + b
    a -= b; //a is equal to a - b
    a *= b; //a is equal to a * b
    a /= b; //a is equal to a / b
    a %= b; //a is equal to a % b

    //relation operators

    a == b; //checks if a is equal to b
    a != b; //checks if q is not equal to b
    a > b; //checks wether a is larger than b
    a < b; //checks whether a is smaller than b
    a >= b; //greater or equal to
    a <= b; //smaller ore qual to
    //we can use a cast operator where we put a desired type in braces (), and the data after it will be converted to that type
    int c = (int) 2.50 + (int) 5.75; //2.50 becomes 2 and 5.75 becomes 5 so answer is 7
    int size = sizeof a; //sizeoff operator returns number of bytes occupied by a variable of type int
    printf("%d\n", size);
    printf("%d", c);
    return 0;
}