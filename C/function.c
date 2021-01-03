#include <stdio.h>
//in this file we will crate 3 functions in a single program, as practise
//1. write a function that finds the greatest common divisor
//2. write a function to calculate the absolute value of a number
//3. write a function to compute square root of a number

int gcd(int u, int v); //we can declare the function here, and the file will work despite the function being declared after main function
float absoluteValue(float x);
float squareRoot(float x);
int main ( )
{
    int greatestCommonDivisor = gcd(150, 35); //save our result of the function in variable
    printf("The gcd of 150 and 35 is %d\n", greatestCommonDivisor);

    float a1 = absoluteValue(-15.3);
    float a2 = absoluteValue(-16.4);
    float a3 = absoluteValue(7);

    printf("-15.3 becomes: %.2f\n", a1);
    printf("-16.3 becomes: %.2f\n", a2);
    printf("7 becomes: %.2f\n", a3);

    float number = squareRoot(16);
    printf("The square root of 16 is %.2f", number);

}

int gcd(int u, int v)
{
    int temp;

    while ( v != 0) //standard algorithm to find greatest common divisor
    {
        temp = u % v;
        u = v;
        v = temp;
    }
    return u;
}

float squareRoot(float x)
{
    const float epsilon = .00001;
    float guess = 1.0;
    float returnValue = 0.0;

    if (x < 0)
    {
        printf("Negative argument to squareRoot\n");
        returnValue = -1.0;
    }
    if (returnValue != -1.0)
        {
        while (absoluteValue(guess * guess - x) >= epsilon) //algorithm to find squareroot
        {
            guess = (x / guess + guess ) / 2.0;
        }
        returnValue = guess;

    }
    return returnValue;
}

float absoluteValue(float x)
{
    if (x < 0) //if our input is negative, we make it positive to become absolute, otherwise return input
    {
        x = -x;
    }
    return x;
}