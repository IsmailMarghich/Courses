#include <stdio.h>
#include <stdlib.h>

//in this file we try using enums
int main ()
{
        enum Company {Google, Facebook = 99, Xerox, Yahoo, Ebay, Microsoft}; //our list of valid variables for 'Company', we can also set a custom value for facebook

        enum Company xerox = Xerox; //here we set variables that can only be filled with things from enum Company
        enum Company google = Google;
        enum Company ebay = Ebay;
        enum Company facebook = Facebook;

        //we print them all out, we get their index in the enum Company as output
        printf("The value of xerox is: %d\n", xerox);
        printf("The value of google is: %d\n", google);
        printf("The value of ebay is: %d", ebay);
        printf("The value of facebook is: %d", facebook);
        return 0;

}