#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define SIZE 7 //our 7 long array
int main ( )
{
    //conversion functions can convert variables to different datatypes
    char string[10] = "10";

    int integer = atoi(string); //atoi converts ascii to integer
    double doublepoint = atof(string); (string); //atof converts ascii to double
    long longint = atol(string); // atol converts ascii to long
    float floatingpoint = atoff(string); //atoff converts ascii to float

    printf("%d\n", rand()); //rand will return a random number without set limit

    srand(time(0)); //we can set a seed by using our time as seed, so everytime its a new seed

    printf("%d\n", rand() % 5 + 1); //we can add a maximum with % and our max number, we add 1 because numbers start from 0

    char command[10];
    strcpy(command, "ls"); //copying a command into a string
    system(command); //with system we can run commandline commands

    printf("%s", getenv("HOME")); //with getenv we can find an environment via a directory name

    //to more easily copy over arrays in C, there is the memcpy and memmove function

    int array[7] = {1,2,3,4,5,6,7};
    int targetarray[7] = {0,0,0,0,0,0,0};
    memcpy(targetarray, array, SIZE * sizeof(int)); //we copy our array into target array,
                                                 // we specify our mem size by multiplying length of array and size of int

    for (int i = 0; i < 7; i++) //loop to print out all the items of the array
        printf("\n%d", targetarray[i]);

    int secondarray[7] = {0,0,0,0,0,0,0};

    memmove(secondarray, array, SIZE * sizeof(int)); //memmove is similar to memcpy, but with memcpy the memory cells cant overlap
    //memmove on the other hand has to check before hand, making it slightly slower but it can handle overlapping memory because of this
    for (int i = 0; i < 7; i++) //loop to print out all the items of the array
        printf("\n%d", secondarray[i]);

    char str[10] = "Copy me !";

    char * copiedstring = strdup(str); //strdup copies a string into a pointer
    printf("\n%s", copiedstring);

    char * halfcopiedstring = strndup(str, 5); //with strndup we can specify how many bytes to be copied
    printf("\n%s", halfcopiedstring);
}