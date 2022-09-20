#include<stdio.h>
int checkBinary(int a){
    while(a>0){
        int rem= a%10;
        a/=10;
        // printf("rem= %d\n", rem);
        if (rem!=0 && rem!=1)return 0;
    }
    return 1;
}

void main(){
    int a;
    printf("Enter the number: ");
    scanf("%d", &a);

    if(checkBinary(a))printf("%d is binary\n." , a);
    else printf("%d is not binary.\n" , a);
}