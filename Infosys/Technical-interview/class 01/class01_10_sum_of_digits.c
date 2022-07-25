#include<stdio.h>

int sumOfDigits(int sum, int a){
    if (a<10) return sum + a;
    sum+=a%10;
    return sumOfDigits(sum, a/10);
}

int main(){
    int a;
    printf("Enter a number: ");
    scanf("%d", &a);
    printf("The sum of digits of %d is %d\n", a, sumOfDigits(0, a));
}