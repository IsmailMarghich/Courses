#include <stdio.h>

//bitmasks can be used to set multiple bits in a byte to either on or off with bitwise operators
//for example u can use a bitmask that's made up of zeros except for 1 field and with an and operator to check whether a bit is turned on or off
int main() {
    int flags = 15; //0000 1111
    int mask = 182; //1011 0110

    //whatever 1s there are in mask, will set those bits to 1 in the flags variable
    flags = flags | mask; //1011 1111

    int flags1 = flags; //0000 1111
    int mask1 = mask; //1011 0110

    //we can use and and complement operator to turn off bits specified by 1 in the mask, the reason we do complement is so zeros dont get changed.
    flags1 = flags1 & ~(mask1); // 0000 1001 //as u can see, only bits that are both 1 in flags and mask are changed

    int flags2 = flags; //0000 1111
    int mask2 = mask; //1011 0110

    //we can use XOR bitwise operator to toggle bits in the byte specified by our bitmask
    flags2 = flags2 ^ mask2; //1011 1001

    return 0;
}