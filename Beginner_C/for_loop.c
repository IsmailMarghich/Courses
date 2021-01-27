#include <stdio.h>

//this program will count from 1 to an integer that the user can enter, and prints the sun of these numbers
int main() {
    unsigned int count = 0;
    unsigned int sum = 0;

    printf("Enter the number of integers you want me to sum: \n");
    setlinebuf(stdout); //flush the print statement
    scanf("%d", &count);

    for (int i = 1; i <= count; ++i) {
        printf("%d\n", i);
        sum += i;
    }
    printf("The sum is : %d", sum);
    return 0;

}