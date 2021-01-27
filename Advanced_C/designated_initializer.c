#include <stdio.h>

//with designated initializers we can initialize values of variables when we declare them, saving time
int main() {
    int numbers[10] = {1, 2,
                       3, [3 ... 9] = 10}; //with the braces we can specify indexes which can all be set to a certain value
    for (int i = 0; i < 10; i++)               //here everything between index 3 and 9 is assigned as 10
        printf("%d ", numbers[i]);
}