#include<stdio.h>

int checkArmstrong(int a){
    int sum=0;
    while(a>0){
        int rem= a%10;
        sum+= rem*rem*rem;
        a/=10;
    }
    return sum;
}

int main(){
    int a;
    printf("Enter the number: ");
    scanf("%d", &a);
    if(a==checkArmstrong(a))printf("%d is an armstrong number.\n");
    else printf("%d is not an armstrong number.\n");
}