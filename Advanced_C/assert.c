#include <stdio.h>
#include <assert.h>

//assert can be used to prevent a program from running by asserting that a certain expression must be true or 1, with assert()
int main() {
    int age;

    printf("Enter your age: ");
    scanf("%d", &age);

    assert(age >= 18); //assert errors out if the assertion is failed, when age is under 18
    printf("Assert succeeded"); //this will only print if assertion is met

    return 0;
}
