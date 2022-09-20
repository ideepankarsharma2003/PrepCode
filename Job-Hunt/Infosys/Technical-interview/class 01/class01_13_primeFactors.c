#include<stdio.h>
int checkPrime(int a){
    int count=0;
    for (int i = 2; i <=a; i++)
    {
        /* code */
        if (a%i==0)count++;
    }
    if (count==1) return 1;
    return 0;
}

int main(){
    int a;
    printf("Enter the number: ");
    scanf("%d", &a);

    printf("The prime factors of %d are: ", a);
    for (int i = 1; i <= a; i++)
    {
        /* code */
        if (a%i==0 && checkPrime(i))printf("%d   ", i);
    }
    printf("\n");
    
}