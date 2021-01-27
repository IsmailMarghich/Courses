#include <stdio.h>
//stacks are datastructures where we can store data with the LIFO idea, last in, first out.
//that means the last item added to the stack, will be the first one to be removed, like a stack of plates
//stacks are used to store function calls for example, because those are also last in first out
//they can also be used when implementing an undo operation in a text editor, or browser history
//we can implement a stack with an array or linked list, in this file we will use an array
//a stack array is simpler to implement, however it cannot grow dynamically in size like a stack. but this is for the concept of a stack
#define MAXSIZE 5
struct stack {
    int stk[MAXSIZE]; //max size of array
    int top; //the length of array, distance from bottom to top
};
typedef struct stack STACK;

STACK s; //naming our stack to s

void push(void);

int pop(void);

void display(void);

int main() {
    int choice; //the users choice
    int option = 1; //variable for checking whether user has to choose an option
    s.top = -1; //top is how large our stack is

    while (option) {
        printf("--------------------------------\n");
        printf("1 -> push\n");
        printf("2 -> pop\n");
        printf("3 -> display\n");
        printf("4 -> exit\n");
        printf("--------------------------------\n");

        printf("Enter your choice\n");
        setlinebuf(stdout);
        scanf("%d", &choice);

        switch (choice) { //we use switch to determine what option the user wants
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                display();
                break;
            case 4:
                return 0;

        }
        fflush(stdin);
        printf("Do you want to continue (type 1 or 0\n"); //option for the user to continue
        setlinebuf(stdout);
        scanf("%d", &option);
    }
}

void push() //function to add to stack
{
    int num = 0;
    if (s.top == (MAXSIZE - 1)) { //check whether stack is full
        printf("Stack is full\n");
        return;
    } else {
        printf("Enter the element to be pushed\n");
        setlinebuf(stdout);
        scanf("%d", &num); //get number from user
        s.top = s.top + 1; //increase our stack size by one
        s.stk[s.top] = num; //set the new top in our array
        //each time we increment the top value by one, so the new tops get moved in the array in different places
    }
}

int pop() //function to remove top value
{
    int num = 0;
    if (s.top == -1) //if s.top is -1, our stack is empty
    {
        printf("Stack is empty\n");
        return (s.top);
    } else {
        num = s.stk[s.top]; //getting the top value
        printf("element %d has been popped\n", s.stk[s.top]);
        s.top = s.top - 1; //decrease our stack length, which means we cant reach the top value anymore
    }
    return (num);
}

void display() {
    int i = 0;
    if (s.top == -1) {
        printf("Stack is empty\n");
        return;
    } else {
        printf("\n Status of the stack: \n");
        for (i = s.top; i >= 0; i--) //a for loop to go through whole stack
            printf("%d\n", s.stk[i]); //print stack element each time
    }
    printf("\n");
}