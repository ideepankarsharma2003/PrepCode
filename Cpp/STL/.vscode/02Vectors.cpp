#include<bits/stdc++.h>
using namespace std;
int main(){
    vector<int> v1; // ----> {}
    cout<<"The size of vector v1 is: "<< v1.size()<< endl; // ---> 0

    v1.push_back(10); // ---> {10}
    v1.push_back(11); // ---> {10, 11}
    cout<<"The size of vector v1 is: "<< v1.size()<< endl; // ---> 2
    v1.pop_back();
    cout<<"The size of vector v1 is: "<< v1.size()<< endl; // ---> 1

    /**
     * Segmentation Fault ----> if you push back 10^7 times
     * 
     */


    v1.push_back(12); // ---> {10, 12}
    v1.push_back(13); // ---> {10, 12, 13}

    v1.clear(); // ------> erase all the elements at once , {}
 
    cout<<"The size of vector v1 is: "<< v1.size()<< endl; 


    vector<int> v2(4, 0); // ----> {0, 0, 0, 0}
    vector<int> v3(4, 16); // ----> {16, 16, 16, 16}

    // copying vectors
    vector<int> v4(v2.begin(), v2.end()); // copy v2 into v4    ---> [)
    vector<int> v5(v3); // copy v3 into v5

    vector<int> vec1;
    vec1.push_back(1); // vec1.emplace_back(1) -----> emplace_back() takes lesser time than push back
    vec1.push_back(3);
    vec1.push_back(2);
    vec1.push_back(5); // -> {1, 3, 2, 5}

    vector<int> vec2(vec1.begin(), vec1.begin()+2); // ---> {1, 3}



    cout<<"v1: ";
    for(auto it:v1){
        cout<<it<<' ';
    }cout<<endl;

    cout<<"v2: ";
    for(auto it:v2){
        cout<<it<<' ';
    }cout<<endl;

    cout<<"v3: ";
    for(auto it:v3){
        cout<<it<<' ';
    }cout<<endl;

    cout<<"v4: ";
    for(auto it:v4){
        cout<<it<<' ';
    }cout<<endl;

    cout<<"v5: ";
    for(auto it:v5){
        cout<<it<<' ';
    }cout<<endl;

    cout<<"vec1: ";
    for(auto it:vec1){
        cout<<it<<' ';
    }cout<<endl;

    cout<<"vec2: ";
    for(auto it:vec2){
        cout<<it<<' ';
    }cout<<endl;




    // lower bound, upper bound

    // swap()----> swap(v1, v2)
    // begin(), end(), rbegin(), rend()





    // Defining 2D vectors
    vector<vector<int>> vec2D; 
    
    vector<int> vec1D1;
    vec1D1.push_back(10);
    vec1D1.push_back(11);
    
    vector<int> vec1D2;
    vec1D2.push_back(20);
    vec1D2.push_back(21);
    vec1D2.push_back(22);
    vec1D2.push_back(23);

    vec2D.push_back(vec1D1);
    vec2D.push_back(vec1D2);

    cout<<"vec2D= {";
    for(auto it: vec2D){
        cout<<'[';
        for(auto jt: it){
            cout<<jt<<' ';
        }cout<<"], ";
    }cout<<'}'<<endl;

    // Traditional Way
    cout << "vec2D= {";
    for (int i = 0; i < vec2D.size(); i++)
    {
        /* code */
        cout << '[';
        for (int j = 0; j < vec2D[i].size(); j++)
        {
            /* code */
            cout<< vec2D[i][j]<<' ';
        }cout<<"], ";
    }cout<<'}'<<endl;




    // define 10 x 20
    vector<vector<int>> vec10x20(10, vector<int>(20, 0));

    // array of vectors
    vector<int> arr[4];



    // 3D-Vectors
    // 10 x 20 x 30
    // int arr[10][20][30]
    vector<vector<vector<int>>> vec3D(10, vector<vector<int>>(20, vector<int>(30, 0)));
    cout << "The size of vector vec3D is: " << vec3D.size() << endl; 
    cout << "The size of vector vec3D[0] is: " << vec3D[0].size() << endl; 
    cout << "The size of vector vec3D[0][0] is: " << vec3D[0][0].size() << endl; 
}