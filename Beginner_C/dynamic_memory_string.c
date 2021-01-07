#include <stdio.h>
#include <stdlib.h>

//in this program we print a string from users input, but we have to manage the memory and ask how much memory the user wants to use
//also we must prevent the program from running out of memory
int main()
{
    int size;
    char *text = NULL;

    printf("Enter limit of the text: \n");
    setlinebuf(stdout);
    scanf("%d", &size);

    text = (char *) malloc(size * sizeof(char));

    if (text != NULL)
    {
        printf("Enter some text: \n");
        scanf(" ");
        gets(text);

        printf("Inputted text is: %s\n", text);
    }

    free(text);
    text = NULL;
    return 0;
}
