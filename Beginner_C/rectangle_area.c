#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) //add commandline arguments to our main
{ //we set the default value to 1
    double area = 1; // width * height
    double width = atoi(argv[1]); //width is first argument //atoi converts it from char to double
    double height = atoi(argv[2]); //height is second argument
    double perimeter = 1; // height + with * 2

    area = width * height; //calculate the height and perimeter
    perimeter = (height + width) * 2.0;

    printf("The width is : %lf\n", width); //print it all out
    printf("The height is : %lf\n", height);
    printf("The area is : %lf\n", area);
    printf("The perimeter is : %lf\n", perimeter);

    return 0;
}
