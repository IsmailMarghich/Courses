#include <stdio.h>
#include <complex.h>
int main ( )
//complex numbers are imaginary numbers in the form of a + b ^i where b stays a negative number after squaring
//complex and imaginary numbers might seem pointless at first but are used in the fields of engineering, electricity, physics and maths
{
    double complex cx = 1.0 + 3.0*I; //we can use the macro I to make 3.0 part of the complex part of a number
    double complex cy = 1.0 - 4.0*I;

    printf("cx = %.2f%+.2fi\n", creal(cx), cimag(cx)); //creal gets the real part of a complex number, cimag gets the imaginary part

    double complex sum = cx+cy; //we can add the numbers together
    printf("cx = %.2f%+.2fi\n", creal(cy), cimag(cy));
    printf("The sum of cx + cy = %.2f%+2.fi\n", creal(sum), cimag(sum));

    return 0;

}
