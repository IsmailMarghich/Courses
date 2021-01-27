#include <stdio.h>
#include <stdlib.h>
//in this file we look at functions that format values for us


// Function declarations
int isEven(const int);

int isPrime(const int);

int main() {

    char string[100];

    sprintf(string, "%Hello this is a number: %d", 55); //sprintf formats the string and stores it in a char array
    //unlike printf which sends output to the console, it returns a formatted string
    puts(string);

    //we can scan from files directly with fscanf function, below is an example program using this function
    //the purpose of this program is to have a file full of numbers and printing these numbers out, and whether they are prime, odd or even numbers
    FILE *fPtrIn = NULL;

    int num = 0, success = 0;

    fPtrIn = fopen("numbers.txt", "r");

    if (fPtrIn == NULL) {
        // Unable to open file hence exit
        printf("Unable to open file.\n");
        printf("Please check whether file exists and you have read/write privilege.\n");
        exit(EXIT_FAILURE);
    }

    // File open success message
    printf("File opened successfully. Reading integers from file. \n\n");

    // Read an integer and store read status in success. (initial read)
    success = fscanf(fPtrIn, "%d",
                     &num); //fscanf will read formatted input from a file stream, in this case our file with numbers

    do { //loop to go through each number
        if (isPrime(num)) //use our helper functions to check the numbes
            printf("Prime number found: %d\n", num);
        else if (isEven(num))
            printf("Even number found: %d\n", num);
        else
            printf("Odd number found: %d\n", num);

        // Read an integer and store read status in success.
        success = fscanf(fPtrIn, "%d", &num);

    } while (success != -1); //this will go through all numbers until we read the end of file

    fclose(fPtrIn);

    return 0;
}

/*
 * Check whether a given number is even or not. The function
 * return 1 if given number is odd, otherwise return 0.
 */
int isEven(const int num) {
    return !(num & 1);
}


/*
 * Check whether a number is prime or not.
 * Returns 1 if the number is prime otherwise 0.
 */
int isPrime(const int num) {
    int i = 0;;

    // Only positive integers are prime
    if (num < 0)
        return 0;

    for (i = 2; i <= num / 2; i++) {
        /*
         * If the number is divisible by any number
         * other than 1 and self then it is not prime
         */
        if (num % i == 0) {
            return 0;
        }
    }

    return 1;
}
