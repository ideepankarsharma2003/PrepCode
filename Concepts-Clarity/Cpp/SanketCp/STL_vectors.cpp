#include<bits/stdc++.h>
using namespace std;

/**
 * VECTORS 
 */

int main(){

    // Declaring Vectors
    // vector<type> variable;
    vector<int> v1; // without default size and default value
    vector<int> v2(10); // with default size= 10 but without default value
    vector<int> v3(10, 2); // with default size=10 and default value= 2
    vector<int> v4{10, 20, 30}; // array like initialization
    vector<int> v5(v4.begin(), v4.end()); // initialization from another vector

    int arr[]= {1, 2, 3, 4, 5};
    vector<int> v6(arr, arr+5);



    // Adding elements to the vector
    vector<int> v;
    for (int i = 0; i < 5; i++) v.push_back(i); // O(1) operation
    for (int i = 0; i < 5; i++) cout<<v[i]<<" ";

    

    
}