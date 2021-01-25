#include <stdio.h>
#include <stdlib.h>

int compare_ints(const void *, const void *);
void exitfunction(void);
//in this file we will look at different useful functions from the stdlib.h library
int main ( )
{
    //quicksort is one of fastest algorithms to sort arrays in C
    int array[5] = {3,2,1,7,5};
    //it takes an array, size of array, size of each array element in bits, and a function to compare the members of array

    qsort(array, 5, sizeof(int), compare_ints);

    for (int i = 0; i < 5; i++)
        printf("%d\n", array[i]);

    atexit(exitfunction); //the atexit function will exit the program and also run functions specified in the arguments before exiting
    abort(); //the abort function is for abnormal stops, file buffers are not flushed, streams are not closed, and temp files are not deleted
            //this is used to detect fatal erorrs, where it is important that the data above isn't lost. In an exit() the above data would get lost
}
void exitfunction(void)
{
    puts("I get run at exit");
}
int compare_ints(const void *p1, const void *p2) //function to compare integers
{
    const int i1 = * (const int *) p1;
    const int i2 = * (const int *) p2;
    return i1 - i2;
}