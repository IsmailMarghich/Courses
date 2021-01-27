#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
//sometimes a program needs more than the default data types that C offers, so we can make our own, we call them abstract datatypes
//in this file we will make a linked list data type, which is a list with nodes, where each node contains a value pointing to the next node in the list

// self-referential structure
struct node //our struct that will store data of node
{
    int value; //value of node
    struct node *next; //pointer to the next node
};

struct node* createNode(int);
void insertNodeAtTheBeginning();
void insertNodeAtTheEnd();
void insertNodeAtPosition();
void deletePosition();
void search();
void updateValue();
void display();

struct node *newnode, *ptr, *prev, *temp;
struct node *head = NULL, *tail = NULL; //we have a tail and head in our linked list, we set them to null at the start

int main() {
    int ch = '\0';

    while (true)
    {
        printf("\n---------------------------------\n");
        printf("\nOperations on a linked list\n");
        printf("\n---------------------------------\n");
        printf("\n1.Insert node at beginning");
        printf("\n2.Insert node at end");
        printf("\n3.Insert node at a specific position");
        printf("\n4.Delete Node from any Position");
        printf("\n5.Update Node Value");
        printf("\n6.Search Element in the linked list");
        printf("\n7.Display List");
        printf("\n8.Exit\n");
        printf("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
        printf("\nEnter your choice: ");
        setlinebuf(stdout); //asking the user what he wants to do
        scanf("%d", &ch);

        switch (ch)
        {
            case 1:
                insertNodeAtTheBeginning();
                break;
            case 2:
                insertNodeAtTheEnd();
                break;
            case 3:
                insertNodeAtPosition();
                break;
            case 4:
                deletePosition();
                break;
            case 5:
                updateValue();
                break;
            case 6:
                search();
                break;
            case 7:
                display();
                break;
            case 8:
                printf("\n...Exiting...\n");
                return 0;
            default:
                printf("\n...Invalid Choice...\n");
                break;
        }
    }
    return 0;
}

/*
 * Creating Node
 */
struct node* createNode(int val)
{
    newnode = (struct node *)malloc(sizeof(struct node)); //allocate memory to our first node
    if (newnode == NULL)
    {
        printf("\nMemory was not allocated");
        return 0;
    }
    else
    {
        newnode->value = val; //setting our value
        newnode->next = NULL; //setting our next to null
        return newnode;
    }
}

void insertNodeAtTheBeginning()
{
    int val = 0;

    printf("\nEnter the value for the node: ");
    scanf("%d", &val);
    newnode = createNode(val);
    if (head== tail && head == NULL) //if we dont have tail or head we create a head
    {
        head = tail = newnode;
        head->next = NULL;
        tail->next = NULL;
    }
    else
    {
        temp = head; //if they already is a tail and head
        head = newnode; //we swap the head with new node, and set new node next value to old head
        head->next = temp;
    }
}

void insertNodeAtTheEnd()
{
    int val = 0;

    printf("\nEnter the value for the Node: ");
    scanf("%d", &val);
    newnode = createNode(val);
    if (head == tail && tail == NULL) //if there is no head, we make this our head
    {
        head = tail = newnode;
        head->next = NULL;
        tail->next = NULL;
    }
    else
    {
        tail->next = newnode; //we set tails next to new tail
        tail = newnode; //tail becomes the new node
        tail->next = NULL; //the tail ends so set next to NULL
    }

    printf("\n----INSERTED----");
}

void insertNodeAtPosition()
{
    int pos, val, cnt = 0, i;

    printf("\nEnter the value for the Node: ");
    scanf("%d", &val);
    newnode = createNode(val);
    printf("\nEnter the position ");
    scanf("%d", &pos);
    ptr = head;
    while (ptr != NULL)
    {
        ptr = ptr->next;
        cnt++;
    }
    if (pos == 1) //if position is at the beginning we check if there is heads or tail, and add it
    {
        if (head == tail && head == NULL)
        {
            head = tail = newnode;
            head->next = NULL;
            tail->next = NULL;
        }
        else
        {
            temp = head;
            head = newnode;
            head->next = temp;
        }
        printf("\nInserted");
    }
    else if (pos>1 && pos<=cnt) //if we find a position in range
    {
        ptr = head;
        for (i = 1;i < pos;i++) //we try to go to the position
        {
            prev = ptr;
            ptr = ptr->next;
        }
        prev->next = newnode; //the previous node next, becomes the inserted node
        newnode->next = ptr; //the new node next becomes the old next of the previous node
        printf("\n----INSERTED----");
    }
    else
    {
        printf("Position is out of range");
    }
}


void deletePosition()
{
    int pos, cnt = 0, i;

    if (head == NULL)
    {
        printf("List is empy\n");
        printf(":No node to delete\n");
    }
    else
    {
        printf("\nEnter the position of value to be deleted: ");
        scanf(" %d", &pos);
        ptr = head;
        if (pos == 1)
        {
            head = ptr->next;
            printf("\nElement deleted");
        }
        else
        {
            while (ptr != NULL)
            {
                ptr = ptr->next;
                cnt = cnt + 1;
            }
            if (pos > 0 && pos <= cnt) //similar process of finding the position to delete
            {
                ptr = head;
                for (i = 1;i < pos;i++)
                {
                    prev = ptr;
                    ptr = ptr->next;
                }
                prev->next = ptr->next; //we set the previous node next, to the node after the one we want to delete, cutting it off
            }
            else
            {
                printf("Position is out of range ");
            }
            free(ptr);
            printf("\nElement deleted");
        }
    }
}


void updateValue()
{
    int oldval, newval, flag = 0;

    if (head == NULL)
    {
        printf("List is empty\n");
        printf(":No nodes in the list to update\n");
    }
    else
    {
        printf("\nEnter the value to be updated: ");
        scanf("%d", &oldval);
        printf("\nEnter the new value:");
        scanf("%d", &newval);
        for (ptr = head;ptr != NULL;ptr = ptr->next) //we find the old value
        {
            if (ptr->value == oldval)
            {
                ptr->value = newval; //simply set old value to new one
                flag = 1;
                break;
            }
        }
        if (flag == 1)
        {
            printf("\nUpdated Successfully");
        }
        else
        {
            printf("\nValue not found in List");
        }
    }
}

void search()
{
    int flag = 0, key, pos = 0;

    if (head == NULL)
    {
        printf("List is empty\n");
        printf(":No nodes in the list\n");
    }
    else
    {
        printf("\nEnter the value to search ");
        scanf("%d", &key);
        for (ptr = head;ptr != NULL;ptr = ptr->next) //we iterate over list to find value
        {
            pos = pos + 1;
            if (ptr->value == key)
            {
                flag = 1; //if we find value we set flag to 1, otherwise we say we couldnt find it
                break;
            }
        }
        if (flag == 1)
        {
            printf("\nElement %d found at %d position\n", key, pos);
        }
        else
        {
            printf("\nElement %d not found in list\n", key);
        }
    }
}

void display()
{
    if (head == NULL)
    {
        printf("List is empty\n");
        printf(":No nodes in the list to display\n");
    }
    else
    {
        for (ptr = head;ptr != NULL;ptr = ptr->next) //we iterate over the whole list
        {
            printf("%d->", ptr->value); //and print the whole list
        }
    }
}
//the advantage of linked lists is that their memory usage is consistent unlike with arrays where there could randomly be assigned a lot of memory
//it also allows us to insert in between nodes, which you cannot do in an array
