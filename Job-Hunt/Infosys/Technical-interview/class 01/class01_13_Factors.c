#include<stdio.h>
int main(){
    int a;
    printf("Enter the number: ");
    scanf("%d", &a);

    printf("The factors of %d are: ", a);
    for (int i = 1; i <= a; i++)
    {
        /* code */
        if (a%i==0)printf("%d   ", i);
    }
    printf("\n");
    
}