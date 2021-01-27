#include <stdio.h>
#include <stdlib.h>
//print the contents of a file in reverse order, using positioning and functions like ftell() and fseek()
#define FILENAME "reverse.txt"

int main() {
    FILE *fp = NULL; //creating a file pointer
    int count = 0;
    int i = 0;

    fp = fopen(FILENAME, "r");

    if (fp == NULL) {
        return -1;
    }

    fseek(fp, 0, SEEK_END); //setting file pointer to end of file

    count = ftell(fp); //get our current position

    while (i < count) //while zero is smaller than count
    {
        i++; //increment
        fseek(fp, -i, SEEK_END); //and move back in the file
        printf("%c", fgetc(fp)); //print a char
    }
    //get position of file pointer
    printf("\nFile has been reversed");
    fclose(fp);
    fp = NULL;
    return 0;
}