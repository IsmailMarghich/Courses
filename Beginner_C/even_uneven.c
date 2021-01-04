#include <stdio.h>

int main() {
    int number, remainder;

    printf("Enter a number to be tested: ");
    setlinebuf(stdout); //flush the print statement
    scanf("%d", &number);
    remainder = number % 2;

    if (remainder == 0)
        printf("The number is even");
    else
        printf("The number is uneven");
    return 0;

}