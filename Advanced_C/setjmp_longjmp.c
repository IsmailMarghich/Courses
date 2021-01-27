#include <stdio.h>
#include <setjmp.h>
#include <stdlib.h>

//setjmp and longjmp are functions that can be used to manipulate control flow in C
//setjmp is like try in languages like c++ and java, longjmp can be used like throw
//the advantage of setjmp and longjmp over goto is that they can jump to any function in the file, goto is limited within a function
jmp_buf buf; //declaring our global buffer variable

void myFunction() //second function to demonstrate jumping between functions
{
    printf("in my function()\n");
    longjmp(buf, 0);

    printf("you will never see this because we long jumped"); //this wont run because we jump out
}

int main() {
    int i = setjmp(
            buf); //we store the state of the stack in a buffer variable (funcitons calls are variables are stored in stack memory)
    printf("i=%d\n", i);

    if (i != 0) //to prevent infinite loop we exit when the i gets assigned a new value
        exit(0);
    myFunction(); //we call the function to see it jumping back to to the start of main function

    longjmp(buf, 42); //we then jump back, the second argument is what the jump should return

    printf("Does this line get printed?\n");
    return 0;
    //we can modify the second return argument to return numbers that we can then use in if statements to break out of the program as recovery.
    //this way we can jump out of a loop and error out so we can exactly see where the error happens
}