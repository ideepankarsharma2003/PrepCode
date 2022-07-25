#include<stdio.h>

int reverse(int sum, int a){
    if (a<10) return sum*10 + a;
    int rem= a%10;
    sum= sum*10 + rem;
    a= a/10;
    return reverse(sum, a);
}

int main(){
    int a;
    printf("Enter the number: ");
    scanf("%d", &a);

    if (a==reverse(0, a))printf("%d is a palindrome\n", (a));
    else printf("%d is not a palindrome\n", (a));
}