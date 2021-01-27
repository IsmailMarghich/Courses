#include <stdio.h>

int main(int argc, char *argv[]) {
    int numberOfArguments = argc;
    char *argument1 = argv[0]; //command line arguments are stored in argv
    char *argument2 = argv[1];

    printf("Number of arguments: %d\n", numberOfArguments);
    printf("Argument 1 is the program name : %s\n", argument1);
    printf("Argument 2 is the command line argument: %s", argument2);

    return 0;
}