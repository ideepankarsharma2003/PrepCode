#include<stdio.h>

int main(){
    int n;
    printf("Enter the number of terms: ");
    scanf("%d", &n);
    printf("The fibonacci series upto %d terms: ", n);
    int first=0, second=1, third=0;
    if (n==1)printf("%d ", first);
    else printf("%d %d ", first, second);
    for (int i = 2; i < n; i++)
    {
        /* code */
        third= first+second;
        printf("%d ", third);
        first= second;
        second= third;
        
    }
    printf("\n");

}