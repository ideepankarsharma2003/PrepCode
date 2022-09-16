#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
/**
 * @brief Pointers
 * 1. Null Pointer -----> NULL
 * 2. Generic Pointers/ Void Pointer ----> any data type
 * 
 */
int main(){
    /**
     * malloc() ----> returns a void pointer{pointer to base address}, initializes with garbage values
     * 
     * 
     * (cast_type*)calloc(n, element_Size) -----> initializes with 0
     * 
     * realloc(ptr, new_size)
     * free(ptr) -----> deallocate the memory 
     * 
     */
    int *ptr1= (int*)malloc(5*sizeof(int)); // typecaste to integer pointer address
    for(int i=0; i<5; i++)
    {
        /* code */
        printf("%d ", *ptr1);
        ptr1++;
    }
    printf("\n");


    
    
    int *ptr2= (int*)calloc(10, sizeof(int)); // typecaste to integer pointer address
    for(int i=0; i<5; i++)
    {
        /* code */
        printf("%d ", *ptr1);
        ptr1++;
    }
    printf("\n");

    printf("ptr1 is freed !!!");
    printf("ptr2 is freed !!!");
    ptr1= realloc(ptr1, 0); // deallocate using realloc()
    assert(ptr1!=NULL);
    fflush(stdout);
    // free(ptr2);
    free(ptr2);
}