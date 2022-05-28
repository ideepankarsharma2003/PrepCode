#include<bits/stdc++.h>
using namespace std;

int main(){
    /**
     * @SET
     * unindexed , sorted
     * 
     */
    array<int, 5> arr= {2, 5, 3, 1, 3}; // unique elements ---> {1, 2, 3, 5}

    set<int> s;
    for (int i = 0; i < 5; i++){
        /* code */
        int x;
        cin>>x; s.insert(x);  // log(N) ---> time
    }

    for(auto it: s){
        cout<<it<<" ";
    }
     
}