#include <stdio.h>
#include <stdlib.h>
///reading files
int main ( )
{
    FILE *pfile = NULL; //creating a file pointer
    char str[60];

    pfile = fopen("myfile.txt", "r+");//opening a file in Read mode

    if (pfile == NULL) //if we cant find the file we exit
    {
        perror("Error opening file");
        exit(1);
    }
    if( fgets(str, 60, pfile) != NULL) //otherwise we use fget string function to get a string thats 60 chars long from the file
    {
        printf("%s", str); //print the string
    }
    fputs("written to file", pfile);
    if( fgets(str, 60, pfile) != NULL)
    {
        printf("%s", str);
    }
    fclose(pfile); //close file
    pfile = NULL; //close pointer
    return 0;
}
