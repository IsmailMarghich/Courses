#include <stdio.h>

int main() {
    int a = 25; //11001
    int b = 77; //1001101
    int c = 0;

    //the basic C bitwise operators

    c = a &
        b; //the and & bitwise operator will set a bit to 1 only if both bits are 1 in the other binary numbers, otherwise its 1
    printf("%d\n", c); //9 =  1001

    c = a | b; // the or | operator will set a bit to 1 if its 1 on either binary number, otherwise it will set it to 0
    printf("%d\n", c); //9 3 = 1011101

    c = a ^ b; //similar to the or operator, but it will set bit to zero if they are 1 in both binary numbers
    printf("%d\n", c); //84 = 1010100

    c = ~(a); //twos complement will flip the bits and turn it into a negative number with -1 added onto it
    printf("%d\n", c); //a is 25 and becomes -26

    //there are also right and left shifts in C which will shift the bits in that direction specified by a number
    int number = 3; //...011
    int result = 0;

    //left shift will move bits to the left by x amount of bits specified by the number afterwards

    result = number << 1; // 3 becomes ...110 which is 6
    printf("%d\n", result);

    //right shift will move bits to the right by x amount of bits specified by the number afterwards
    result = number >> 1; //3 becomes ...01 which is 1
    printf("%d", result);
    //if its bits are shifted outside of the field, they are lost
    return 0;
}