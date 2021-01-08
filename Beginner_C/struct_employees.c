#include <stdio.h>
#include <stdlib.h>

//create a structure that stores information of employees with their name, hire date and salary
//ask the user for the information for a second employee and print out both employees' data
//a struct can store multiple variables

struct employee { //create a struct with our data
    char name[30];
    char date[15];
    float salary;
};
int main ( ) {
    struct employee emp1 = {"Mike", "8-1-2020", 23432.00f}; //set our first employee struct
    printf("\n Name: %s", emp1.name);
    printf("\n Hiredate: %s", emp1.name);
    printf("\n salary: %f", emp1.salary);

    struct employee emp2; //lets create an empty struct for our employee

    printf("\nEnter employee information: \n"); //ask user for input and assign it to emp2's struct values
    printf("Name: ");
    setlinebuf(stdout);
    scanf("%s", emp2.name);

    printf("\nEnter hiredate: ");
    setlinebuf(stdout);
    scanf("%s", emp2.date);

    printf("\nEnter salary:");
    setlinebuf(stdout);
    scanf("%f", &emp2.salary);

    printf("\n Name: %s", emp2.name); //print it all out
    printf("\n Hiredate: %s", emp2.name);
    printf("\n salary: %f", emp2.salary);

    return 0;
}