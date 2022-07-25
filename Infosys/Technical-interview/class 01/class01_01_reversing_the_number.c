#include<stdio.h>
void main(){
    int a, b, c;
    printf("Enter the number: ");
    scanf("%d", &a);
    
    printf("The reverse of the number is: ");
    int n= 0;
    while (a>0)
    {
        /* code */
        int rem= a%10;
        a/=10;
        // printf("a= %d\n",a );
        // printf("n= %d\n",n );
        n= n*10+ rem;
        printf("%d", rem);
    }
    printf("\n");
    // printf("The reverse of the number is: %d\n", n);
    
}