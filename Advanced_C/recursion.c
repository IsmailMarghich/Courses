#include <stdio.h>
//recursive functions are functions that call themselves directly or indirectly

int factorial(int n);

int main() {
    printf("%d", factorial(6)); //6 * 5 * 4 * 3 * 2 * 1
}

//a recursive function needs a base case to prevent it from infinitely looping
int factorial(int n) {
    if (n == 0) //if we dont reach base case
        return (1);
    return (n * factorial(n - 1)); //we multiply n by itself -1
}