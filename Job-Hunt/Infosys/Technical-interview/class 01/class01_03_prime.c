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
    printf("Enter a number: ");
    scanf("%d", &a);
    if(checkPrime(a))printf("%d is a prime number.\n", a);
    else printf("%d is not a prime number.\n", a);

}