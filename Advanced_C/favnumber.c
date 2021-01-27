#include <stdio.h>
#include "favnumber.h"

//this file is to demonstrate how we can divide the program in header files
//the getfavoritenumber function is defined in a header file, but we can still use it here by including it
int main() {
    printf("%d\n", getfavoritenumber());
    return 0;
}
