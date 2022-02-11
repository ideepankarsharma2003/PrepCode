#include<iostream>
using namespace std;
#define MAX 1000 // assuming max size to be 1000 ----> (0-999)
int oneHot[MAX]={0}; 

void checkOneHot(){

    for(int i=0; i<MAX; i++){
        if(oneHot[i] !=0){
            int num = oneHot[i];
            for (int j = 0; j < MAX; j++)
            {
                if (i != j)
                {
                    /* code */
                    if (num==oneHot[j])
                    {
                        /* code */
                        // cout<<num<<endl;
                        cout << "False" << endl;
                        return;
                    }
                    
                }
            }
        }
    } 
    
    cout << "True" << endl;
}

void check(int arr[], int n){
    int drr[n]={0};
    for (int i = 0; i < n; i++)
    {
        /* code */
        int num= arr[i];
        oneHot[num]++;

    }

    checkOneHot();
    
}

int main(){
    int n=6;
    int arr[]= {1, 2, 2, 1, 1, 3};
    check(arr, n);
}