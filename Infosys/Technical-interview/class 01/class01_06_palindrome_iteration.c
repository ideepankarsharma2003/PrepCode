#include<stdio.h>

int reverse(int a){
    int sum= 0;
    while (a>0)
    {
        /* code */
        int rem= a%10;
        sum= sum*10 + rem;
        a= a/10;
    }
    
    return (sum);
}

int main(){
    int a;
    printf("Enter the number: ");
    scanf("%d", &a);

    if (a==reverse(a))printf("%d is a palindrome\n", (a));
    else printf("%d is not a palindrome\n", (a));
}