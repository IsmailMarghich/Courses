#include <stdio.h>
#include <stdbool.h>


int main() {
    struct date //defining struct date
    {
        int year;
        int month; //defining variables in the struct
        int day;
    } today;

    struct date *datep; //making a pointer refer to a struct

    datep = &today; //set the pointer to our today struct
    datep->day = 9; //setting the day to 9 we use structure pointer operator -> instead of  .
    printf("%d\n", datep->day); //print it out,

    struct intpointers //creating a struct made of pointers
    {
        int *p1;
        int *p2;
    } pointers;

    int i1 = 100, i2;

    pointers.p1 = &i1;
    pointers.p2 = &i2;
    *pointers.p2 = -97;

    printf("p1 = %i\n", *pointers.p1);
    printf("p2 = %i\n", *pointers.p2);

    return 0;
}


