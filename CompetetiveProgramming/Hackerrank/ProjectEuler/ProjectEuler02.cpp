#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int a0 = 0; a0 < t; a0++)
    {
        long n;
        cin >> n;
        long long int first= 1, second= 2, third= 0, sum=0;
        while(third<n){
            if (second%2==0)sum+=second;
            third= first+second;
            first= second;
            second= third;
        }
        cout<<sum<<endl;
        
    }
    return 0;
}