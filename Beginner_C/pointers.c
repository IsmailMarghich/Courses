#include <stdio.h>

//pointer challenge
//write a program that creates an integer variable with a hard-coded value. Assign that variables address to a pointer variable
//display as output the adress of the pointer, the value of the pointer, and the value of what the pointer is pointing to

void copyString (char *to, char *from);
int lenString (const char *str);
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

    copyString(string2, string1);
    printf("%s\n", string2);

    printf("%d\n", lenString("stringlength"));
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
    const char *lastAdresss = str; //this is our pointer that goes to the end
    while ( *lastAdresss )
        ++lastAdresss; //we keep moving in the string until we reach the end
    return lastAdresss - str; //then substract the end pointer with start pointer (if u call an array in a pointer it goes to first pointer) which returns the length

}