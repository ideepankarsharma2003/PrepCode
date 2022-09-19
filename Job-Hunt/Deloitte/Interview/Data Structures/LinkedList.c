#include<stdio.h>
#include<stdlib.h>

typedef struct Node
{
    /* data */
    int data;
    struct Node* next;
}Node;

/**
 * Functions of Linked List:
 * 1. createNode(int data) returns Node*
 * 2. insertNodeBeginning(Node* head, int data) returns head
 * 
 */

Node* createNode(int data){
    Node*p= (Node*)malloc(sizeof(Node));
    p->data= data;
    p->next= NULL;
    return p;
}

Node *insertNodeBeginning(Node* head, int data)
{
    Node* node= createNode(data);
    node->next= head;
    head= node;
    return head;
}

int main(){

}