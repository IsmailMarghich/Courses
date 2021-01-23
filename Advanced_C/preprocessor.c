#include <stdio.h>
//the C preprocessor is run before the code gets compiled, usually to substitute text in the code with a macro and giving the compiler hints
//in this file we will look at some preprocessor definitions and operators we can use
#define NUMBER 5 //defining a constant
#define CONDITION 1

//with pragma we can tell the compiler what to do
#pragma GCC poison scanf //poison will disable a function
//#pragma GCC warning "This is a warning"
//#pragma GCC error "This is an error"
#pragma GCC message "This is a message" //these messages will be printed as a compiler message
int main ( )

{
    printf("%d\n", NUMBER); //print constant
#undef NUMBER //we can un define our constant with #undef
    int NUMBER = 0;
    printf("%d\n", NUMBER); //

#if CONDITION == 1
    printf("with #if we can use conditional logic with definitions");
#else
    printf("with #else similar to C's else we can run code if earlier if condition isn't met\n");
#endif //here we stop the conditions

#ifdef defined //with ifdef we can check if a macro is defined or not
    printf("this macro is defined\n")
#else
    printf("this macro is not defined\n");
#endif
}