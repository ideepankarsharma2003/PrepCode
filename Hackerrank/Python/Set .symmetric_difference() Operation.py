# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
arr1 = set(map(int, input().split()))
b= int(input())
arr2 = set(map(int, input().split()))

ans= arr1.symmetric_difference(arr2)
print(len(ans))