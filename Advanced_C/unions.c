#include <stdio.h>

//this file is all about unions, unions are similar to structs where they can store data together, but it can store multiple different types of data
//it also does not use memory for unused variables, unlike structs
//unions store the different types of variable in the same memory spot unlike structs which does that separately, thus saving you memory
//the issue with unions however is that only one member of a union can be accessed at a time, and only the first member can be initialized
//thus unions should used when saving memory is important and when u have specialized data
int main() {
    union car {
        int i;
        float j; //a union will allocate memory the same as the largest element in union
        int k;
    };
    union car car1, car2, *carpointer = &car2; //we declare 2 normal unions and 1 pointer union pointing to the second union
    printf("Memory size occupied by data:%zu\n", sizeof(car1)); //float are 4 bytes, so it prints 4
    car1.j = 10.0; //assigning values to our unions works just like structs
    printf("%f\n", car1.j);
    printf("%d\n",
           car1.i);//this will return random numbers(memory address) because only 1 value can be accessed and initialized at a time
    car1.i = 5;
    printf("%d\n", car1.i);//now that car1.i is initialized, it can be printed
    printf("%f\n",
           car1.j); //however this will again return the wrong number, because car1.i has already been initialized, there is only 1 spot

    carpointer->i = 6; //here we can use our pointer to set the i variable in union car2
    printf("%d", carpointer->i); //we use -> for pointers just like with structs
    return 0;
}