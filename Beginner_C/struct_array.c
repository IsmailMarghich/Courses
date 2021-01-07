#include <stdio.h>

//a struct can store multiple variables
//we can store multiple structs in an array
int main ( )
{
    struct date //defining struct date
    {
        int year;
        int month; //definding variables in the struct
        int day;
    };
    //here we create an array with structures in them, and initialize few
    struct date mydates[5] = { {2021,1,7}, {2021,1,8}, {2021,1,9}};
    printf("%d", mydates[0].year);
    return 0;
}