# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
arr1 = set(map(int, input().split()))
b= int(input())
arr2 = set(map(int, input().split()))

ans= arr1.intersection(arr2)
print(len(ans))