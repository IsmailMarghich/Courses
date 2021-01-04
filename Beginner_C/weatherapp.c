#include <stdio.h>
#include <stdlib.h>
//Create a program that used a 2d array with hardcoded values for rainfall over the past 5 years
//The program will find the total rainfall for each year, the average yearly rainfall and the average rainfall for each month

#define MONTHS 12
#define YEARS 5

int main() {
    //initialize rainfall data for 2011-2015
    float rain[YEARS][MONTHS] = {
            {4.3, 4.3, 4.3, 3.0, 2.0, 1.2, 0.2, 0.2, 0.4, 2.4, 3.5, 6.6}, //2011
            {8.5, 8.2, 1.2, 1.6, 2.4, 0.0, 5.2, 0.9, 0.3, 0.9, 1.4, 7.3}, //2012
            {9.1, 8.5, 6.7, 4.3, 2.1, 0.8, 0.2, 0.2, 1.1, 2.3, 6.1, 8.4}, //2013
            {7.2, 9.9, 8.4, 3.3, 1.2, 0.8, 0.4, 0.0, 0.6, 1.7, 4.3, 6.2}, //2024
            {7.6, 5.6, 3.8, 2.8, 3.8, 0.2, 0.0, 0.0, 0.0, 1.3, 2.6, 5.2} //2025
    };
    int year, month;
    float yearlyaverage, total, subtotal;
    float monthlyaverage;

    printf("YEAR\t\tRAINFALL (inches)\n");
    //loop to print total rainfall for each year
    for (year = 0, total = 0; year < YEARS; year++) {
        for (month = 0, subtotal = 0; month < MONTHS; month++) {
            subtotal += rain[year][month]; //we add the 12 months value to subtotal, we dont have to reset it for each year, as its done in the for loop
        }
        printf("%5d \t%.1lf\n", 2010 + year, subtotal); //print the total rainfall for each year
        total += subtotal;
    }
    printf("\n The yearly average is %.lf inches.\n\n", total / YEARS);

    printf("MONTHLY AVERAGES:\n\n");
    printf(" Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec\n");

    //loop to print average monthly rainfall
    for (month = 0; month < MONTHS; month++) { //we loop over each month
        for (year = 0, subtotal = 0; year < YEARS; year++) { //in each year
            subtotal += rain[year][month]; //we grab the total of each month
        }
        printf("%.2lf ", subtotal / YEARS); //then we print the average of that month, and continue to the next month
    }
    return 0;

}