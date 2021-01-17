#include <stdio.h>
//we can use bit operators to pack data into single integers, which saves memory
int main ( )
//this program will ask the user to input a number, and then it will check whether nth bit of the number is 1 or not
//it should also set that nth bit of the given number as 1
//this serves as an exercise of storing data in bits in a single integer
{
    int num, position, newNum, bitStatus;
    setlinebuf(stdout);
    // Input number from user
    printf("Enter any number: ");
    scanf("%d", &num);

    // Input bit position you want to set
    printf("Enter nth bit to check and set (0-31): ");
    scanf("%d", &position);

    // Right shift num, position times and perform bitwise AND with 1
    bitStatus = (num >> position) & 1; //we get the bit we wanna change at the start and & it with 1, which is 1 in binary
    printf("The %d bit is set to %d\n", position, bitStatus);

    //Left shift 1, n times and perform bitwise OR with num
    newNum = (1 << position) | num; //we left shift on 1 which is ..0001 in binary, and then OR to change the bit in number to 1
    printf("\nBit set successfully.\n\n");


    printf("Number before setting %d bit: %d (in decimal)\n", position, num);
    printf("Number after setting %d bit: %d (in decimal)\n", position, newNum);

    return 0;
}