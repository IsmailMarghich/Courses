#include <stdio.h>
#include <math.h>
#include <stdlib.h>

//in this file we will go over some special type of functions in C
inline static int
inlinefunction(double n); //when using inline on a function it suggests the compiler to run this function first
//the inline function must be static

_Noreturn void
noreturnfunction(); //the _Noreturn specifier was introduced in C11, and it used to suggest users and the compiler the function doesnt return
//this means the compiler can do optimizations that it wouldn't be able to do with void functions, as those still return nothing, while _Noreturn simply exit
int main() {
    double n = 4.0;
    inlinefunction(n);
    noreturnfunction();
}

inline static int inlinefunction(double n) //function to return n to the power of n
{
    fprintf(stdout, "%f", pow(n, n));
}

void noreturnfunction() {
    abort(); //this function doesnt return anything, so we abort
}
