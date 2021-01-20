#include <stdio.h>
//in this file we will learn about macros and make our own
//macros are similar to functions, but they are defined in the preprocessor and can make a programmers time easier, we have used macros before
#define PLUS(a,b) \
printf("%d", a+b);
//normally macros are only one a single line but with \ we can use multiple lines
int main ( )
{
    int a = 5;
    int b = 5;
    PLUS(a,b);//making use of our PLUS macro to print the sum of 2 ints
}