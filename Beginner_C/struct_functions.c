#include <stdio.h>
#include <stdlib.h>

//create a C program that creates a structure pointer and passes it to a function
//structure should have: itemName - pointer, quantity - int, price - float, amount - float (stores quantity * price)

//create a function called readitem that reads in the name, quantity and price and put it in a structure
//create a function named print item that takes this structure from readitem function and prints the content of the structure, using pointers


struct item //making our item structure
{
    char *itemName;
    int quantity;
    float price;
    float amount;
};

void readItem(struct item *i);

void printItem(struct item *i);

int main() {
    struct item itm; //setting our structure in itm
    struct item *pItem; //making a pointer

    pItem = &itm; //setting pItem pointer to a pointer in struct
    pItem->itemName = (char *) malloc(30 * sizeof(char)); //allocating memory for our pointer

    if (pItem == NULL) //if our pointer is empty we leave the program
        exit(-1);

    readItem(pItem); //read input from user -> structure
    printItem(pItem); //print the structure
    free(pItem->itemName); //free up the memory we assigned for pointer
    return 0;
}

void readItem(struct item *i) {
    printf("Enter your product name: "); //read users input with scanf and use -> to assign it to struct
    setlinebuf(stdout);
    scanf("%s", i->itemName);

    printf("\nEnter price: ");
    setlinebuf(stdout);
    scanf("%f", &i->price);

    printf("\nEnter the quantity: ");
    setlinebuf(stdout);
    scanf("%d", &i->quantity);

    i->amount = (float) i->quantity * i->price; //calculate total amount with quantity and price


}

void printItem(struct item *i) //print all of the values in struct
{
    printf("\nName: %s", i->itemName);
    printf("\nPrice: %f", i->price);
    printf("\nQuantity %d", i->quantity);
    printf("\nTotal amount: %.2f", i->amount);
}