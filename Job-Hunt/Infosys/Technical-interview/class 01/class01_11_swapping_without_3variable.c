#include<stdio.h>
void main(){
    int a, b, c;
    printf("Enter the value of a: ");
    scanf("%d", &a);
    printf("Enter the value of b: ");
    scanf("%d", &b);
    
    a= a+b;
    b= a-b;
    a= a-b;

    printf("a= %d \n", a);
    printf("b= %d \n", b);
}