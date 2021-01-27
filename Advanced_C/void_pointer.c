#include <stdio.h>

//void pointers are pointers without a specific type
//we need to cast a void pointer everytime we want to use it
int main() {
    void *voidpointer = NULL;
    int a = 5;
    voidpointer = &a; //asign pointer to this variable a= 5


    printf("%d", *(int *) voidpointer); //cast it to int with *(int *)

    //our void pointer is flexible since we can use it for every datatype
    // it is useful for functions that need to accept multiple different datatypes

    return 0;
}