#include <stdio.h>

//a struct can store multiple variables
int main() {
    struct date //defining struct date
    {
        int year;
        int month; //definding variables in the struct
        int day;
    } today; //here we can also add the name after the struct, to initialize the struct in today

    today.year = 2021;//we can assign variables to structs by using . to access members
    today.month = 1;
    today.day = 7;

    printf("%d %d %d\n", today.year, today.month, today.day);
    struct date tommorow = {.year = 2021, .month = 1, .day = 8}; //we can also declare the struct in one go

    printf("%d %d %d", tommorow.year, tommorow.month, tommorow.day);


}
