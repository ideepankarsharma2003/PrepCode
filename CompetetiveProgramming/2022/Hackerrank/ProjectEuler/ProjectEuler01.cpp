#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int a0 = 0; a0 < t; a0++)
    {
        int n;
        cin >> n;

        long long int x3 = (n - 1) / 3;
        long long int sigma3 = ((x3) * (2 * 3 + (x3 - 1) * 3)) / 2;
        // cout<<"Sigma3= "<< sigma3<<endl;
        long long int x5 = (n - 1) / 5;
        long long int sigma5 = ((x5) * (2 * 5 + (x5 - 1) * 5)) / 2;
        // cout<<"Sigma5= "<< sigma5<<endl;
        long long int x15 = (n - 1) / 15;
        long long int sigma15 = ((x15) * (2 * 15 + (x15 - 1) * 15)) / 2;
        // cout<<"Sigma15= "<< sigma15<<endl;

        cout << sigma3 + sigma5 - sigma15 << endl;
    }
    return 0;
}
