#include <stdio.h>
#include <stdlib.h>

//queues are similar to stacks, where they store data but in a FIFO structure, first in, first out.
// the first item added to the list, will be removed first. similar to real life queues
//we will be using an array for this queue, we have to check whether the array is full when we queue an item, since its a fixed size
#define MAX 50

void enqueue();

void dequeue();

void display();

int queue_array[MAX];
int rear = -1; //the front is the first item in queue, the rear is the last one
int front = -1;

int main() {
    int choice;
    while (1) {
        printf("1. Insert element to queue \n");
        printf("2. Delete element from queue \n");
        printf("3. Display all elements of queue \n");
        printf("4. Quit \n");
        printf("Enter your choice: ");
        setlinebuf(stdout);
        scanf("%d", &choice);

        switch (choice) //with this switch we run different functions based on users input
        {
            case 1:
                enqueue();
                break;
            case 2:
                dequeue();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(1);
            default:
                printf("Wrong choice \n");
        }
    }
}

void enqueue() {
    int add_item;

    if (rear == MAX - 1) //if array is full we dont add
        printf("Queue overflow \n");
    else {
        if (front == -1) //if our front is -1 we set it to zero, cause were adding the first item
            front = 0;
        printf("Insert the element in queue : ");
        setlinebuf(stdout);
        scanf("%d", &add_item);
        rear = rear + 1; //increase the index of rear
        queue_array[rear] = add_item; //adding item to the queue on the new rear index
    }
}

void dequeue() {
    if (front == -1 || front > rear) //if the front is empty
    {
        printf("Queue underflow \n");
        return;
    } else {
        printf("%d has been deleted from queue\n", queue_array[front]);
        front = front + 1; //we move our front, thus ignoring the first entry in queue
    }
}

void display() {
    int i;
    if (front == -1)
        printf("Queue is empty\n");
    else {
        printf("Queue is : \n");
        for (i = front; i <= rear; i++) //we start from front and iterate over array until we reach the end
            printf("%d ", queue_array[i]); //and we print each item from queue
        printf("\n");
    }
}