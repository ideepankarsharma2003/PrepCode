#include<bits/stdc++.h>
using namespace std;

array<int, 5> arr1; // initialized with zeroes ----> {0, 0, 0, 0, 0}
int main(){
    
    cout<<"arr1: ";
    for(auto it:arr1){
        cout<<it<<' ';
    }cout<<endl;


    array<int, 5> arr2; // initialized with garbage values;
    
    cout<<"arr2: ";
    for(auto it:arr2){
        cout<<it<<' ';
    }cout<<endl;
    


    arr2= {1, 2, 3}; // ----> {1, 2, 3, 0, 0}
    arr2= {1}; // ----> {1, 0, 0, 0, 0}
    arr2= {0}; // ----> {0, 0, 0, 0, 0}


    arr2.fill(10); // ----> {10, 10, 10, 10, 10}

    cout<<"arr2: ";
    for(auto it:arr2){
        cout<<it<<' ';
    }cout<<endl;

    arr2= {1, 2, 3, 4, 5 };
    int idx= 2;
    cout<<"Item at index "<< idx<< " is: "<< arr2.at(idx)<< endl;
    cout<<"The size of arr2 is: "<< arr2.size()<< endl;
    cout<<"The front item of arr2 is: "<< arr2.front()<< endl;
    cout<<"The back item of arr2 is: "<< arr2.back()<< endl;

    /**
     * Iterators
     * begin()------> first element
     * end()------> last empty space
     * rbegin()------> first element(reverse)
     * rend()------> last empty space(reverse)
     */

    cout << "arr2: ";
    for(auto it = arr2.begin(); it!=arr2.end(); it++){
        cout<<*it<<' ';
    }cout<<endl;

    cout << "arr2(reverse): ";
    for(auto it = arr2.rbegin(); it!=arr2.rend(); it++){
        cout<<*it<<' ';
    }cout<<endl;

    cout << "arr2(reverse): ";
    for(auto it = arr2.end()-1; it>=arr2.begin(); it--){
        cout<<*it<<' ';
    }cout<<endl;

}