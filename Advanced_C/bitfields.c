#include <stdio.h>
#include <stdbool.h>
//in the bitpacks.c file we used integers to store data and with bitwise operators we added and read data
//however it is easier to do this with structs, and we call these bitfields
//in this file we will have a program that contains the following information about a box in a struct bitfield
//the box can be opaque or transparent, a fill color using 8 different colors (3bits), a border can be shown or hidden, a border color with the same 8 colors (3bits)
//a border cna use one of three line styles, (2bits), this is 10 bytes, so were gonna have to use 2 bytes with 6 bits padded

//line styles
#define SOLID   0
#define DOTTED  1
#define DASHED  2

// primary colors
#define BLUE    4
#define GREEN   2
#define RED     1

// mixed colors, we use or and primary colors to create the other ones
#define BLACK   0
#define YELLOW  (RED | GREEN)
#define MAGENTA (RED | BLUE)
#define CYAN    (GREEN | BLUE)
#define WHITE   (RED | GREEN | BLUE)

const char * colors[8] = {"black", "red", "green", "yellow",   "blue", "magenta", "cyan", "white"}; //our different colors

struct box_props {
    bool opaque                 : 1;
    unsigned int fill_color     : 3;
    unsigned int                : 4; //rest of byte we leave empty
    bool show_border            : 1;
    unsigned int border_color   : 3;
    unsigned int border_style   : 2;
    unsigned int                : 2; //rest of byte we leave empty
};

void show_settings(const struct box_props * pb); //function to display the box, it will use a pointer

int main(void) {

    /* create and initialize box_props structure */
    struct box_props box = {true, YELLOW , true, GREEN, DASHED};

    printf("Original box settings:\n");
    show_settings(&box);

    box.opaque = false; //after initializing our bitfield struct, we can now change it up
    box.fill_color = WHITE;
    box.border_color = MAGENTA;
    box.border_style = SOLID;
    printf("\nModified box settings:\n");
    show_settings(&box);

    return 0;
}
void show_settings(const struct box_props * pb)  //with our pointer we go to different parts of the struct and check for values to print out
{
    printf("Box is %s.\n", pb->opaque == true ? "opaque": "transparent");
    printf("The fill color is %s.\n", colors[pb->fill_color]); //here we grab it from our color char array
    printf("Border %s.\n",  pb->show_border == true ? "shown" : "not shown");
    printf("The border color is %s.\n", colors[pb->border_color]); //here we grab it from our color char array
    printf ("The border style is ");

    switch(pb->border_style) //this field can be 0, 1 or 2 so its a bit trickier so we use switch with cases
    {
        case SOLID  : printf("solid.\n"); break;
        case DOTTED : printf("dotted.\n"); break;
        case DASHED : printf("dashed.\n"); break;
        default     : printf("unknown type.\n");
    }
}