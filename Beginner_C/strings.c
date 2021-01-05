#include <stdio.h>
#include <string.h>
#include <ctype.h>

//lets make use of some default C library string functions

int stringlength(const char string[]);

int main (void)
{
    char string1[100] = "Hello";
    char string2[100] = "Goodbye";
    char stringcopy[100];

    printf("%d\n", strlen(string1));//strlen returns length of string

    strcat(string1, string2); //strcat concatenates first string with second string, and assigns the new string to first string
    printf("%s\n", string1);


    strcpy(stringcopy, string1); //copies the second string to first string
    printf("%s\n", stringcopy);

    strncpy(string1, stringcopy, 100); //this is for when u dont have a set size for the char array, and you can set the max size of the char array with third argument
    printf("%s\n", string1);

    printf("%d\n", strcmp("A", "A")); //strcmp compares the string, returns 0 if equal, -1 if first string is smaller than second string, 1 if first string is bigger than second string
    printf("%d\n", strcmp("A", "B"));

    printf("%d\n", strncmp("AAAA", "AAAB", 3)); //strncmp we can specify till how many items we compare, starting from the left
    printf("%d\n", strncmp("AAAA", "AAAB", 4));

    ////searching and tokenizing functions for strings

    //we have to use pointers for certain string functions

    char str[] = "The flying dutchman"; //setting our string
    char ch = 'd'; //setting the character we wanna look for
    char *pChar_pointer = NULL; //initializing our pointer
    pChar_pointer = strchr(str, ch); //the strchr string will find the a character specified in second argument in a string in first argument
    printf("%s\n",pChar_pointer); //it then displays the rest of the string from the character it finds

    //with tokenizing we can separate a string based on a token

    char tokenstring[] = "Hello - Hi - Hey"; //our string
    char s[2] = "-"; //we are gonna separate based on the dash -
    char *token; //our pointer towards token

    token = strtok(tokenstring, s); //we grab the first token

    while ( token != NULL) //and then we iterate over the whole string
    {
        printf("%s\n", token); //printing the part until the token
        token = strtok(NULL, s); //and then we enter NULL in strok, this will make it go to the next segment
    }
    printf("%c", toupper('g')); //with toupper or tolower function we can convert a character or string (using a loop and iterating) to upper or lowercase


}
