#include <stdio.h>

//in this file we will be using the goto statement for control flow
int main() {
    //goto statement
    const int maximuminput = 5;
    int i = 0;
    double number, average, sum = 0.0;
    for (i = 1; i < maximuminput; ++i) {
        printf("%d. enter a number: ", i);
        setlinebuf(stdout);
        scanf("%lf", &number);
        if (number < 0.0)
            goto jump; //if we have a negative number we jump out of the loop and go to label jump
        sum += number;
    }
    jump: //label jump is define here, and the program will continue executing code under it
    average = sum / (i - 1);
    printf("sum = %.2f\n", sum);
    printf("average = %.2f", average);
    return 0;
    //goto statements interrupt the normal sequential flow of the program, and as a result its harder to follow and maintain
    //I would only recommend goto statements if you wanna move out of a bunch of nested loops
}