#include <stdio.h>

int fibonacci(int i)
{
    if (i == 0)
        return 0;
    if (i == 1)
        return 1;
    return fibonacci(i - 1) + fibonacci(i - 2);
}

int main()
{
    int n;
    printf("Enter the number of terms: ");
    scanf("%d", &n);
    printf("The fibonacci series upto %d terms: ", n);
    for (int i = 0; i < n; i++)
    {
        /* code */
        printf("%d ", fibonacci(i));
    }
    printf("\n");
}