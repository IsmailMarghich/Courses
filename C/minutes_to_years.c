#include <stdio.h>
//the purpose of this program is to convert an amount of  (int) minutes to years and days
int main ( )
{
    int minutes; //set our variables
    double minutes_in_year = 525948.766; //amount of minutes in a year
    double year = 0.0;
    double days = 0.0;
    printf("Enter your amount of minutes: ");
    setlinebuf(stdout); //flush the print statement
    scanf("%d", &minutes); //grab the amount of minutes
    year = (double) minutes / (double) minutes_in_year; //we get the amount of years by diving minutes by the minutes in a year
    days = (double) year * 365; //we get the days by multiplying the amount of years by the days in a year
    printf("%d Minutes is: \n", minutes);
    printf("Year(s): %lf\n", year); //print everything
    printf("Days: %lf", days);
    //we have to make sure our output stays a double, so we use casting when calculating the amount of years and days, (double)



}