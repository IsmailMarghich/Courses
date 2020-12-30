#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//Create a guessing game where users have to guess a number between 0 and 20
//The program will also indicate if the user's guess is too high or low, after 5 tries the game is lost

int main ()
{    //our starting variables
    _Bool win = 0;
    time_t t;
    int guess;
    srand((unsigned) time(&t));
    int randomnum = rand() % 21; //generating a number between 0 and 20

    printf("This is a guessing game\n"); //asking user for input
    printf("I have chosen a number between 0 and 20 which you must guess :\n");
    setlinebuf(stdout); //flush the print statement

    for (int tries = 5; tries > 0; --tries) //starting a loop for 5 tries
    {
    scanf("%d", &guess); //scan for input
    if (guess < 0 || guess > 20) //make sure its between 0 and 20
    {
    printf("please enter a number between 0 and 20\n");
    continue;
    }
    if (guess == randomnum)
    {
    printf("Congrats, you guessed the number\n"); //if guess is correct, update win
    win = 1;
    break;
    }
    else if (guess < randomnum)
    {
    printf("Your guess is lower than the random number\n");
    }
    else if (guess > randomnum)
    {
    printf("Your guess is higher than the random number\n")    ;
    }
    printf("You have %d tries left \n", tries-1); //we do minus one because we ask for input before the loop
    }
    if (!win) //if the user runs out of attempts, (loop is over) and he lost, then we print he lost
    {
        printf("You ran out of tries");
    }
    return 0;
}