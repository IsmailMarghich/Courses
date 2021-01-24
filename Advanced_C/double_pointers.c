#include <stdio.h>
#include <malloc.h>

//double pointers are pointers who point to a pointer which points to a variable
//one of their use cases is when used in function arguments, when a single pointer is used, a copy is made
//because of this u can't modify the variable that the pointer is pointing to, using double pointers u can however since a copy is made of a pointer to a pointer

//the point of this file is to demonstrate these double pointers
void allocateMemory( int ** ptr);
int main ( )
{
    //First we will demonstrate different ways of accessing data using single and double pointers
    int num = 5;

    //A normal pointer singlePointer
    int *singlepointer = NULL;

    //This pointer doublePointer is a double pointer
    int **doublepointer = NULL;

    //Assigning the address of variable num to the single pointer
    singlepointer = &num;

    //Assigning the address of pointer singlePointer to the doublePointer
    doublepointer = &singlepointer;


    // Possible ways to find value of variable num
    printf("\n Value of num is: %d", num);
    printf("\n Value of num using singlePointer is: %d", *singlepointer);
    printf("\n Value of num using doublePointer is: %d", **doublepointer);

    // Possible ways to find address of num
    printf("\n Address of num is: %p", &num);
    printf("\n Address of num using singlePointer is: %p", singlepointer);
    printf("\n Address of num using doublePointer is: %p", *doublepointer);

    // Find value of pointer
    printf("\n Value of Pointer singlePointer is: %p", singlepointer);
    printf("\n Value of Pointer singlePointer using doublePointer is: %p", *doublepointer);

    // Ways to find address of pointer
    printf("\n Address of Pointer singlePointer is:%p",&singlepointer);
    printf("\n Address of Pointer singlePointer using doublePointer is:%p",doublepointer);

    // Double pointer value and address
    printf("\n Value of Pointer doublePointer is:%p",doublepointer);
    printf("\n Address of Pointer doublePointer is:%p",&doublepointer);

    //now we will showcase how we can use double pointers as function arguments
    //we want to allocate memory to a pointer using a function, however a function will make a copy of a pointer passed, which will not work
    int *ptr = NULL;

    allocateMemory(&ptr); //use our allocate memory function on our pointer
    *ptr = 20;

    printf("\n%d", *ptr);

    // free up the memory
    free(ptr);

    return 0;
}
void allocateMemory( int ** ptr) //we use a double pointer as argument, now a copy of a pointer pointing to a pointer is made
{                                                                       //which means we can modify the pointer
    *ptr = (int *) malloc(sizeof(int)); // allocate some memory
}