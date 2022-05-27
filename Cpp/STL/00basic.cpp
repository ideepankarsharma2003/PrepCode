#include<bits/stdc++.h>
using namespace std; // std scope 

namespace lucky{
    int val= 50;

    void me(){
        cout<<"This is me :)"<<endl;
    }
}

struct node
{
    /* data */
    string str;
    int num;
    node(string str_, int num_){
        str= str_;
        num= num_;
    }
};



int main(){
    int val= 10;
    cout<<"The value is "<< val<< endl;
    cout<<"The value is "<< lucky::val<< endl;
    lucky::me();


    node n= node("I'm Node !", 5);
    cout<< n.num<< '\t'<< n.str<<endl;
}