#include <stdio.h>

int main()
{
    int age = 18, dadage = 50; //you can assign values to multiple variables
    printf("your age is %d\n", age);
    age += 2; //we can add to integers
    printf("you grew up 2 years, your age is now %d\n", age);
    printf("your dad's age is %d\n", dadage);
    char firstletter = 'A'; //here we define a char, which is a single character value, we use ' ' here
    printf("The first letter of the alphabet is %c\n", firstletter);
    char name[100] = "Ismail"; //here we define a string with 100 characters limit
    printf("This is a string, my name is %s\n", name);
    float temp = 25.50; //here we define a float because it has numbers after the comma
    printf("It is %g degrees Celsius outside\n", temp); //we use &g instead of &f to avoid trailing zero's
    _Bool bool = 1; //A boolean value is either false or true, where 1 is True and false is zero
    enum primaryColor {
        red, green, blue
    }; //an enum variable means it can only contain certain values specified in the curly braces
    enum primaryColor myColor; //here we declare our own variable based on the enum
    myColor = red; //this should return no error, because red is one of the valid types for the enum
// Here we showcase the different format specifiers in C
    int integervar = 100;
    float floatvar = 330.30;
    double doublevar = 8.44e+11;
    char  charvar = 'W';
    _Bool boolvar = 0;
    char stringvar[100] = "string";
    printf("integervar = %i\n", integervar);
    printf("floatingvar = %f\n", floatvar);
    printf("doublevar = %e\n", doublevar);
    printf("charvar = %c\n", charvar);
    printf("boolvar = %i\n", boolvar);
    printf("stringvar = %s\n", stringvar);
// width format specifier will specify how much numbers after the comma it will print
    float x = 3.123456;
    printf("float with width specifier 2: %.2f", x); //.2 means there will be 2 decimal points
}