#include <stdio.h>

//storage classes describe the scope, the visibility and life-time of a function or variable
extern int globalnumber; //when we use extern it will look for a global variable with that name and use it
extern void globalfunction(void); //it will do the same thing for functions
int staticfunction(); //declaring our static function
int main() {
    //auto
    //the keyword auto is seldom used when declaring variables, as C automatically uses the auto store class, which makes it a local variable
    //however u might use this keyboard to override an external variable, auto variables are only created when they are needed, making them efficient
    auto int autonumber = 5;

    //external
    //the extern keyword tells us the variable is defined elsewhere, not within the same scope
    //the purpose of extern variables is that they can be accessed between different files
    //the extern storage class is used to give a reference of a global variable that is visible to all the program files
    printf("%d\n", globalnumber); //print our global variable
    globalfunction(); //use our global function

    //static
    //the keyword static instructs the compiler to keep the variable in existence during the lifetime of the program
    //when applied to global variables it will cause the variables scope to be restricted to the file in which it is declared
    //this means static variables will main their values between function calls
    printf("%d\n",
           staticfunction()); //print the function call twice to see that the variable keeps increasing between calls
    printf("%d\n", staticfunction());
    //the advantage of using static over global is that its not possible for 2 files to initialize global variables with the same name which would turn in errors
    //because the static variable is local to the file or scope (depending on if its a local or global static)
    //by default all functions are extern, u can access them from other files, however when u use static for a function
    //that function declaration is only for that file, and cant be accessed in another file

    //register
    //the keyword register is used to define local variables that should be stored in registers instead of RAM
    //this will increase performance when accessing the variable but theres a limited amount of register space, so use with caution
    register int x; //this variable will be stored in the CPU's register
    for (x = 1; x <= 15; x++) //this is handy when a variable is accessed a lot, like in a loop as iterable
        printf("%d", x);
    return 0;
    //the C compiler decides whether to actually store the variable in a register or not, and manages that for us. The keyword register is simply a recommendation
}

int staticfunction() {
    static int count = 0; //this variable will keep its value even after the function exists
    count++; //each time the function is called the variable is increased
    return count;
}