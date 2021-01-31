#include <stdio.h>
#include <stdbool.h>
//strings under the hood are arrays of characters, in this file we will create and use them in functions

//we will make 3 functions:
//1 a function that gets the length of a string
//2 a function that concatenates 2 strings
//3 a functio that compares 2 strings to see if they are equal or not
int stringlength(const char string[]);

void concat(char result[], const char str1[], const char str2[]);

bool equalstrings(const char s1[], const char s2[]);

int main() {
    const char string1[] = "bobby";
    const char string2[] = "johnson";
    char result[50];
    int length = stringlength(string1);

    printf("The length of the string is %d\n", length);

    concat(result, string1, string2);
    printf("%s\n", result);

    printf("%d\n", equalstrings("Jason", "Jason")); //returns 1 because theyre the same
    printf("%d", equalstrings("Jason", "Jones")); //returns zero because they are not the same


    return 0;


}

int stringlength(const char string[]) //this function calculates length of string
{
    int count = 0;

    while (string[count] !=
           '\0') //we loop over the string, increasing the count by 1 after each character until we find \0, which ends the string
    {
        ++count;
    }
    return count;
}

void concat(char result[], const char str1[], const char str2[]) //function to concatenate 2 strings
{
    int i, j;

    for (i = 0; str1[i] != '\0'; ++i) //we copy over the first string to a result character array
    {
        result[i] = str1[i];
    }
    for (j = 0; str2[j] !=
                '\0'; ++j) //because the first slots are taken by first string, we add a new counter, and add the second string after the first one
    {
        result[i + j] = str2[j];
    }
    result[i + j] = '\0'; //we add a character end at the end of string
}

bool equalstrings(const char s1[], const char s2[]) {
    int i = 0;
    bool isequal = false;

    while (s1[i] == s2[i] && //we iterate over both strings and compare if theyre equal, or if they reach the end
           s1[i] != '\0' &&
           s2[i] != '\0') {
        ++i;

    }
    if (s1[i] == '\0' && s2[i] == '\0') { //if both of them reached the end, theyre equal
        isequal = true;
    } else //otherwise theyre false
    {
        isequal = false;
    }
    return isequal;
}


