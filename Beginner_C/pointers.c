#include <stdio.h>

//pointer challenge
//write a program that creates an integer variable with a hard-coded value. Assign that variables address to a pointer variable
//display as output the adress of the pointer, the value of the pointer, and the value of what the pointer is pointing to

void copyString (char *to, char *from);
int lenString (const char *str);
void swapint (int *a, int *b);
void squareitself(int * const i);
int main ( )
{
    int number = 15; //making a variable
    int *pnumber = NULL; //making a pointer

    pnumber = &number; //setting the adress of variable to pointer
    printf("%p\n", &pnumber); //print the adress of the pointer /0x
    printf("%d\n", (int)sizeof(pnumber)); //print size of bytes /8
    printf("%p\n", pnumber); //print the adress of variable /0x
    printf("%d\n", *pnumber); //print the variable itself /15

    //void pointers can point to any datatype, we just have to cast it when using in an expression
    int i = 10;
    void *pvoid; //creating void pointer
    pvoid = &i; //link it with integer
    printf("Void pointer points to %d\n", *(int *)pvoid); //here we specify to cast it as an int with *(int *)

    char string1[] = "Hello";
    char string2[10];

    copyString(string2, string1); //copying the string
    printf("%s\n", string2);

    printf("%d\n", lenString("stringlength"));//measuring the length of "stringlength"

    int a = 5;
    int b = 10;

    swapint(&a, &b); //swap the ints
    printf("swapped: %d and %d\n", a, b); //print them out

    int num = 6;
    squareitself(&num); //we pass on the adress of num
    printf("The suqre of 6 is %d\n", num);
}
//function to copy string, using pointers to iterate over both strings
void copyString (char *to, char *from)
{
    while ( *from ) //when we reach the end of a string, the \0 charatcer, it automatically breaks because its equal to 0, so we can use a while loop
        *to++ = *from++; //we set the value of to, to from, and increment both
    *to = '\0'; //when the while loop is done, we mark the end of string with \0
}
//this function will return the length of a string, using pointers

int lenString (const char *str)
{
    const char *lastAdress = str; //this is our pointer that goes to the end
    while ( *lastAdress )
        ++lastAdress; //we keep moving in the string until we reach the end
    return lastAdress - str; //then substract the end pointer with start pointer (if u call an array in a pointer it goes to first pointer) which returns the length

}
void swapint(int *a, int *b) //this function will swap integers with their pointers, as this will edit their value in the main program
{                            //if we were using values we'd only change the variable within the function, not in main
    int temp;

    temp = *a; //we store a into temp
    *a = *b; //we put b in a
    *b = temp; //we put a in b
}
void squareitself(int * const i)
{
    *i = (*i) * (*i); //we set the value of i with i times i, using pointers so its global

}
