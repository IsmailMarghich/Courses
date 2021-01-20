#include <stdio.h>
//in this file we will learn about macros and make our own
//macros are similar to functions, but they are preprocessed, when a macro is called, the macro body is inserted directly into the code, we have used macros before
#define PRINTPLUS(a, b) \
printf("%d\n", a+b);

#define UAREFUNNY(name) \
printf(#name" Is funny\n") //we can use # to insert a token, i,e a variable like in this example

//normally macros are only one a single line but with \ we can use multiple lines
//a macro is faster than a function since it does not need to be compiled and the macro itself can be immediately replaced by its body
int main() {
    int a = 5;
    int b = 5;
    PRINTPLUS(a, b);//making use of our PLUS macro to print the sum of 2 ints
    //its harder to debug a macro because its preprocessed before the program is compiled, it does not have typed arguments.
    //inline functions can be used instead, they can be debugged and have type checking but inline keyword is only a suggestion to the compiler

    UAREFUNNY(Ismail);
    //there are default macros that C offers for us
    printf("%s\n", __FILE__); //returns file name
    printf("%d\n", __LINE__); //returns number of line
    printf("%s\n", __FUNCTION__); //returns name of function
    printf("%s\n", __TIME__); //returns time
    printf("%s\n", __DATE__); //returns date
    printf("%d\n", __STDC__); //returns 1 if current compiler conforms to ISO standard C compiler, 0 if not

    return 0;
}
