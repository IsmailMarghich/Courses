#include <stdio.h>

int main() {
    //with typedef we can create our own name for an excisting datatype
    typedef int numberwithoutdot;
    numberwithoutdot number = 5;
    printf("%d", number);
    return 0;
}