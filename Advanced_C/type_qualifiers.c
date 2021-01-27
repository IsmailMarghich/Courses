#include <stdio.h>

//type qualifiers can be used in front of variables to give the compiler about the intended use of the variables
int main() {
    //const
    //a const variable cannot be changed, this means the compiler can put this variable in readonly memory, which leaves more ram memory for other variables

    const int x = 5; //constant variable
    const int *const pointer; //with pointers, if u use constant before the star, it means the file its point to is constant
    //if const is after the star, it means the address that the pointer points to is constant
    //volatile
    //volatile is the opposite of const, where volatile tells the compiler that this variable will change
    //normally, sometimes variables are cached in registers so accessing this variable would be faster
    //sometimes this is not desirable because of threads needing to access the original location of the variable
    volatile int y = 5; //this variable will not be cached in register, and threads will thus always access the most up to date version of the variable

    //restrict
    //the restrict type qualifier is an optimization hint for the compiler, it means that a certain pointer is the only reference to a certain value
    //because a restrict pointer is the only one pointing to this data, it means the compiler does not to add any additional checks, which improves performance
    int number = 5;
    int *restrict intpointer = NULL; //because this pointer is the only one pointing to this number, we can use restrict so the compiler can optimize the code
    intpointer = &number;
    printf("%d", *intpointer);


    return 0;
}