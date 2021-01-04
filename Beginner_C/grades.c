#include <stdio.h>
#include <stdlib.h>

int main() {
    int grades[10]; //array of grades
    int count = 10; //how many grades are gonna put
    long sum = 0; //the sum of the grades
    float average = 0.0f; //the average

    printf("\nEnter the 10 grades: \n");

    for (int i = 0; i < count; ++i) { //ask the user for input 10 times
        printf("%2u> ", i + 1); //and each time we print what number they are on
        setlinebuf(stdout); //flush the print statement
        scanf("%d", &grades[i]); //grab the grade and put it in the array at index i
        sum += grades[i]; //add the grade to sum
    }
    average = (float) sum / count; //after loop is done, calculate the average and print it

    printf("The average of the ten grades is %f", average);
}
