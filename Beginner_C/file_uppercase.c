#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
//Create a prorgam that converts all characters in a file to uppercase, write the results to a temporary file
//then rename the temporary file to the original file, and remove the temporary filename
//display the content of the original file
#define FILENAME "lowercase.txt"
int main ( ) {
    FILE *fp1 = NULL; //creating 2 file pointers for temporary and original file
    FILE *fp2 = NULL;
    char ch = ' ';

    fp1 = fopen(FILENAME, "r");

    if (fp1 == NULL)
    {
        return -1;
    }

    //creating a temp file
    fp2 = fopen("temp.txt", "w");

    if (fp2 == NULL)
    {
        return -1;
    }

    while ((ch = fgetc(fp1)) != EOF) //going through the whole file until end of file
    {
        if (islower(ch))
        {
            ch = ch-32; //by subtracting with -32 it becomes an uppercase character
        }
        fputc(ch, fp2); //while going through all characters and converting them to uppercase, we add them to temp file
    }
    fclose(fp1);
    fclose(fp2);
    //now we rename temp file to original file
    rename("temp.txt",FILENAME);
    //remove temp file
    remove("temp.txt");

    fp1 = fopen(FILENAME, "r");
    if (fp1 == NULL)

    {
        return -1;
    }

    while ((ch = fgetc(fp1)) !=  EOF) //loop through file and print everything
    {
        printf("%c", ch);
    }
    fclose(fp1);
    fp1 = NULL;
    fp2 = NULL;
    return 0;
}