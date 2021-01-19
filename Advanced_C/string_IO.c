#include <stdio.h>
#include <stdlib.h>


//in this file we will showcase input and output functions for strings in C
int main ( )
{
    char *buffer = NULL; //our pointer to memory allocation
    size_t bufsize = 32;
    size_t characters;
    //in C there are deprecated functions for inputting strings called gets and fgets, but the best one is getline()
    //getline(); takes 3 arguments, first is double pointer to a block allocated with malloc or calloc, its a double pointer
               //second is a pointer to a variable size_t, for the size of the memory pointed to in first parameter
               //third argument is simply the stream from where to read the line
               //the advantage of this function is that it will automatically re allocate memory, making it safe
    buffer = (char *)malloc(bufsize * sizeof(char )); //block of code to allocate memory
    //it is also possible to replace the buffer expression by making a char array and initializing it and putting a poiner to char array as first argument
    if (buffer == NULL)
        exit(1);
    printf("type something: ");
    characters = getline(&buffer, &bufsize, stdin);

    printf("%zu characters were read.\n", characters-1); //minus one to not count end of string
    printf("you typed: %s\n", buffer);
    puts("This is the puts function");//we can use the puts function to simple write to sdtout, it automatically uses newline but it does not support formatting
    //there is also the sputs function which takes a second argument to write to a file

    return 0;
}
