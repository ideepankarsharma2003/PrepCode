#include<iostream>
using namespace std;

int FirstOccurrence(int arr[] , int n, int ele) 
// arr ----> array 
// n ----> number of elements in arr
// ele -----> element to be rearched 
{
    int l=0, u=n-1;
    int mid=(l+u)/2;
    int ans=-1; // by default !!
    while(l<=u)
    {
        if(arr[mid]==ele)
        {
            ans=mid;
            
            // l=mid-1; // ------> correction
            u= mid-1;
        }
        else if(ele>arr[mid])
        {
            l=mid+1;
        }
        else if(ele<arr[mid])
        {
            u=mid-1;
        }
        mid= (l+u)/2;
    }
    return ans;
}

int LastOccurrence(int arr[] ,int n,int ele)
{
    int l=0,u=n-1;
    int mid=(l+u)/2;
    int ans=-1;
    while(l<=u)
    {
    if(arr[mid]==ele)
    {
		ans=mid;
        l=mid+1;
   	}
    else if(ele>arr[mid])
    {
        l=mid+1;
    }
    else if(ele<arr[mid])
    {
        u=mid-1;
    }
        mid= (l+u)/2;
    }
    return ans;
}

int main()
{
    int n,ele;
    cout << "Enter the size of the array" <<endl;
    cin >> n;

    int arr[n];

    cout << "Enter the elements of the array" <<endl;
    for(int i=0;i<n;i++)
    {
        cin >> arr[i];
    }
    cout << "Enter the element whose occurence is to be find" <<endl;
    cin >> ele;
    cout << "First occurence of " << ele <<" is at index " << FirstOccurrence(arr,n,ele) <<endl;
    cout << "Last occurence of " << ele <<" is at index " << LastOccurrence(arr,n,ele) <<endl;
    return 0;
}