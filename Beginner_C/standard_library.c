#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>

int main ( )
{
    int a = 5;
    int b = 10;
    //math functions
    cos(a); //returns cosinus
    sin(a); //returns sinus
    tan(a); //returns tan
    atan(a); //returns tan
    sqrt(a); //returns square root
    floor(a); //rounds down
    log(a); //gets logarithmic

    remainder(a, b); //gets remainder, %

    //utility function

    abs(b); //returns absolute value
    //system("command") //with the system function u can run commandline in your c file
    assert(a > 1); //assert returns error and exits program if evaluation is false

    return 0;
}