#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//the purpose of this program is print all the prime numbers in between 1 and 100 using an array
int main()
{
    int p;
    int i;

    int primes[50] = {0};
    int primeIndex = 2;

    bool isPrime;

    // hardcode prime numbers
    primes[0] = 2;
    primes[1] = 3;

    for(p = 5; p <= 100; p = p + 2) //start outer loop
    {
        isPrime = true;

        for (i = 1; isPrime && p / primes[i] >= primes[i]; ++i) //inner loop to check if number is a prime number
            if (p % primes[i] == 0)
                isPrime = false;

        if (isPrime == true)
        {
            primes[primeIndex] = p;
            ++primeIndex;
        }
    }

    for ( i = 0;  i < primeIndex;  ++i )
        printf ("%i  ", primes[i]);

    printf("\n");
    return 0;
}
