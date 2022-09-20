/**
 * @file FindPivotIndex.cpp
 * @author Deepankar Sharma (deepankarsharma2003@gmail.com)
 * @brief https://leetcode.com/problems/find-pivot-index/
 * @version 0.1
 * @date 2022-02-19
 *
 * @copyright Copyright (c) 2022
 *
 */

#include<iostream>
#include<vector>
using namespace std;

class Solution
{
        int retSum(vector<int> &arr, int startInd, int endIndex)
        {
            int sum = 0;
            for (int i = startInd; i < endIndex; i++)
            {
                /* code */
                sum += arr[i];
            }
            return sum;
        }

    public:
    
        int pivotIndex(vector<int> &nums)
        {
            int n = nums.size();
            for (int i = 0; i < n; i++)
            {
                int sumLeft = retSum(nums, 0, i);
                int sumRight = retSum(nums, i + 1, n);
                if (sumLeft == sumRight)
                    return i;
            }

            return -1;
        }
};

int main()
{
    // vector<int> arr= {1, 7, 3, 6, 5, 6};
    // vector<int> arr= {1, 2, 3};
    vector<int> arr= {2, 1, -1};
    Solution obj;
    cout<<obj.pivotIndex(arr)<<endl;
}