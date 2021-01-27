#include <stdio.h>
#include <ctype.h>

//in this file we will explore input and output functions with chars in C
int main() {
    //input functions
    char ch = 0;
    //we can use both int and char as type definition, since numbers in chars just get converted to characters
    int i = getc(stdin); //getc gets a single character, it needs a file as argument, but stdin can be used as wel
    printf("I read in: %c\n", i);
    printf("I read with getchar: %c\n", getchar); //getchar does the same except that it always uses stdin as file

    //what if we wanted to read a character but ignore whitespaces
    while (isspace(ch = (char) getchar()));
    {
        ungetc(ch,
               stdin); //this ungetc function will push the space back to the stream, and thus the loop continues to the next character
    }
    printf("char is %c\n", ch);

    //output functions
    char output = 'o';
    char output1 = 'c';
    putc(output, stdout); //putc takes a char/int and a file argument, and then puts that value on the stream
    putchar(output1); //putchar is similar but it puts the character on stdout by default

    return 0;
}