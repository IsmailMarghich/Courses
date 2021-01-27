#include <stdio.h>

static int globalnumber = 6; //static means each file will make a copy of this variable instead of using the variable itself
void globalfunction(void) {
    printf("you just used a global function\n");
}