#include <stdio.h>
#include <stdlib.h>

//in this file we will show off how to dynamically allocate memory with malloc, calloc and realloc functions
int
main() {   //with malloc we can manually allocate bytes to the variable, here we use 25 * the size of an integer, to get memory
    int *p1Number = (int *) malloc(25 * sizeof(int));
    //with calloc we can allocating memory with 2 arguments, the number of items and the size of those items
    //it also initializes the bytes to zero
    int *p2Number = (int *) calloc(75, sizeof(int));
    if (!p1Number) //we use an if statement to make sure the memory is allocated
    {
        free(p1Number); //with free function we can free the memory
        p1Number = NULL; //we make sure the pointer is empty after we free the memory
        free(p2Number);
        p2Number = NULL;

        p2Number = (int *) realloc(p2Number,
                                   50); //with realloc we can add additional memory, where the second argument is how many bytes is to be added
        free(p2Number);
        p2Number = NULL;
    }
    //the memory allocated is automatically released after the program ends, but its better to manually release since memory is very valuable on embedded systems
    return 0;
}
