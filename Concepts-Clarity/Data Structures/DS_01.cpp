#include<stdio.h>
int main(){

    /*  @Array 

    // Array Initialization
    int A[5]= {1, 2}; // {1 2 0 0 0 }
    printf("The size of Integer is: %d.\n", sizeof(int));
    int *ptr= A;


    for (int i = 0; i < 5; i++)
    {
        printf("%d ", *ptr);
        // A= A+1; Not possible in C
        ptr++;
    }
    printf("\n ptr= %u", ptr);
    */
    
   char s1[7]= "1234", *p;
   p= s1+2;
   *p= '0';
   printf("s1= %s\n", s1);

   for (int i = 0; i < 7; i++)
   {
        printf("%d ", s1[i]);
   }
   
    
    return 0;
}