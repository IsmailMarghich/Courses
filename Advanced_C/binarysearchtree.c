#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//binary search trees are a data structure where data is stored in nodes, where each node has a left and right sub node
//a binary search tree is ordered in a way where the left sub tree must be smaller than the right tree, this makes searching more efficient
//there is different ways to traverse and display a binary tree, we will cover:
//in order traversal: Left, Root, Right (it will go to left node, then root (parent) node and then right node)
//preorder traversal: Root, Left, Right
//postorder traversal: Left, Right, Root

struct treeNode {
    int data; //our struct is how each node is gonna be represented, its gonna have left and right sub nodes
    struct treeNode *leftpointer;
    struct treeNode *rightpointer;
};

typedef struct treeNode TreeNode; //make our initial tree node and type def it
typedef TreeNode *TreeNodepointer;  //use a pointer to refer to our treenode
void insertNode(TreeNodepointer *treeptr, int value);

void inOrder(TreeNodepointer treePtr);

void preOrder(TreeNodepointer treePtr);

void postOrder(TreeNodepointer treePtr);


int main() {
    int i = 0;
    int item = 0;
    TreeNodepointer rootPtr = NULL; //set initial tree as empty

    srand(time(NULL));
    printf("The numbers the tree starts with: \n");

    //were gonna insert random values into the tree to start with
    for (i = 1; i <= 10; i++) {
        item = rand() % 15;
        printf("%d ", item);
        insertNode(&rootPtr, item);
    }
    printf("\n preOrder traversal: ");
    preOrder(rootPtr);

    printf("\n inOrder traversal: ");
    inOrder(rootPtr);

    printf("\n postOrder traversal: ");
    postOrder(rootPtr);

    return 0;
}

void insertNode(TreeNodepointer *treeptr, int value) {
    if (*treeptr == NULL) //if tree is empty
    {
        *treeptr = malloc(sizeof(TreeNode));

        //memory is allocated, now assign data
        if (*treeptr != NULL) {
            (*treeptr)->data = value; //set the inputted node as value
            (*treeptr)->leftpointer = NULL; //set left and right to null
            (*treeptr)->rightpointer = NULL;
        } else
            printf("No memory available");
    } else {
        if (value < (*treeptr)->data) //if data to insert is less than current node
            insertNode(&((*treeptr)->leftpointer), value); //recursively call function
        else if (value > (*treeptr)->data) //if data to insert is greater than current node
            insertNode(&((*treeptr)->rightpointer), value); //recursively call function
            //this goes on and on until we come to an empty tree, and then the blocks above will assign it a value
        else //if we find a duplicate value we give up
            printf("Dup ");
    }

}

void inOrder(TreeNodepointer treePtr) {
    if (treePtr != NULL) {
        inOrder(treePtr->leftpointer); //Left
        printf("%d->", treePtr->data); //Root
        inOrder(treePtr->rightpointer); //Right
    }
}

void preOrder(TreeNodepointer treePtr) {
    if (treePtr != NULL) {
        printf("%d->", treePtr->data); //Root
        preOrder(treePtr->leftpointer); //Left
        preOrder(treePtr->rightpointer); //Right
    }
}

void postOrder(TreeNodepointer treePtr) {
    if (treePtr != NULL) {
        postOrder(treePtr->leftpointer); //Left
        postOrder(treePtr->rightpointer); //Right
        printf("%d->", treePtr->data); //Root

    }
}