#include <stdio.h>
#include <stdlib.h>
//write a program that takes a file and reads the number of ines
#define FILENAME "lines.txt"
int main ( )
{
    FILE *fp = NULL; //creating a file pointer
    char ch;
    int linescount = 0; //creating our variable store number of lines

    fp = fopen(FILENAME, "r");

    if (fp == NULL)
    {
        printf("File does not exist");
        return -1;
    }
    while ((ch =fgetc(fp)) != EOF) //creating a loop until we find end of file
    {
        if (ch == '\n') //if we find end of line \n
        {
           linescount++; //increase our line count
        }
    }
    fclose(fp);
    fp = NULL;

    printf("Total number of lines are: %d", linescount+1); //we add plus one because we reach EOF before we can count last line
    return 0;
}