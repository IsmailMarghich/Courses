#include <stdio.h>
//we can use ; as a null statement, the compiler will do nothing but wont error out either

int main() {
    for (int count = 0; getchar() != EOF; ++count) //this counts the number of characters in a string
        ; //because the expression is already done in the for statement, we dont need a body and can just place a NULL with ;

}

