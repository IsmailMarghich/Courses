#include <stdio.h>
#include <math.h>

//In the C programming language u modify bits which is important when you are working with drivers or embedded devices
//and it also handy for operating systems to store information about files in so called bit fields, where you can use a bit to indicate permissions for example
//in this file as an introduction to this topic we will create functions to convert binary to decimal numbers and vice versa
int convertBinaryToDecimal(long long n);

long long convertDecimalToBinary(int n);

int main() {

    long long n;
    int decimalnumber;
    int result = 0;

    printf("Enter a binary number: ");
    setlinebuf(stdout);
    scanf("%lld", &n);

    result = convertBinaryToDecimal(n);
    printf("%lld in binary = %d in decimal\n", n, result);

    printf("Enter a decimal number: ");
    setlinebuf(stdout);
    scanf("%d", &decimalnumber);
    result = convertDecimalToBinary(decimalnumber);
    printf("%d in decimal = %lld in binary", decimalnumber, result);

    return 0;
}

int convertBinaryToDecimal(long long n) {
    int decimal = 0, i = 0, remainder = 0;
    while (n != 0) {
        remainder = n % 10; //this will give us 1 or 0 from a digit
        n = n / 10; //moving on to next number
        decimal += remainder * pow(2, i); //calculating the decimal value by multiplying by 2 to the power of digit
        ++i;
    }
    return decimal;
}

long long convertDecimalToBinary(int n) {
    long long binnumber = 0;
    int remainder, i = 1;

    while (n != 0) {
        remainder = n % 2; //here we use 2 because binary numbers are base 2
        n = n / 2; //moving onto next number
        binnumber += remainder * i; //multiply the number by 10x depending on the position
        i = i * 10;
    }
    return binnumber;
}
