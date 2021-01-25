#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main ( )
{
    //we can measure how long process takes with the clock function
    clock_t start = 0, end = 0; //declaring our clock time data types
    double cpu_time = 0.0;

    start = clock(); //set our start time
    for (int i = 0; i < 10; i++) //our process
        500 * 500;
    end = clock(); //set our end time

    cpu_time = (double)(end - start)/CLOCKS_PER_SEC; //we subtract end with time to get the clock time, and divide it to get seconds
    printf("%d\n", cpu_time);

    time_t rawtime = time(NULL); //time function returns seconds since january 1 1970
    printf("%s\n", ctime(&rawtime)); //with ctime function we can convert those seconds into actual dates, it needs a pointer to a time_t variable

    //with localtime function, we access the days, months, hours and other data via a struct

    struct tm* time_data = localtime(&rawtime); //our struct now gets filled with local time data
    printf("This year is %d\n", time_data->tm_year+1900); //printing the year, it starts from year 1900
    printf("%d\n", time_data->tm_mday); //this prints the day of the month
    printf("It is the %dth month\n", time_data->tm_mon+1); //prints month, add 1 because months are from 0 to 11
    printf("%d hours\n", time_data->tm_hour); //the rest prints the time, all achieved by a single function and a struct
    printf("%d minutes\n", time_data->tm_min);
    printf("%d seconds\n", time_data->tm_sec);

    char * ascpointer = asctime(time_data); //we can get the asci time by giving the asctime function our tm struct
                                            //the function returns a char pointer, which we then print to get ascii time
    printf("%s", ascpointer);


}
