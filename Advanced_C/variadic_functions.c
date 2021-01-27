#include <stdio.h>
#include <stdarg.h>

//in this file we will going over some advanced function concepts in C
int variadicfunction(int variable1, ...);

int main() {
    //variadic functions are functions with not just mandatory arguments, but also optional ones, an example of this is the printf function
    //where u can print use multiple arguments, i.e variables to format in the string
    variadicfunction(5, 6); //this function can take as much arguments as it wants
}

int variadicfunction(int variable1,
                     ...) //to add variadic arguments to a function, you add 3 dots ... in the function definition
{

    va_list parg; //pointer for variable arguments
    va_list copy;

    va_start(parg, variable1); //we set the start at the last mandatory argument
    va_copy(copy, parg);

    int variable2 = va_arg(parg,
                           int); //we can constantly call va_arg function to get the first, and then next argument everytime we call it again
    //if we wanna use the same arguments multiple times, we can store a copy of the argument list in a va_list variable
    int copy1 = va_arg(copy, int);
    //we add more variables and assign them to more arguments, we can also use a while loop to iterate over all arguments

    printf("%d\n", variable1 * variable2); //we double the numbers and print them
    printf("%d\n", variable1 * copy1);

    va_end(parg); //va_end cleans the argument list up and sets the pointer to NULL
    va_end(copy);
    return 0;
}