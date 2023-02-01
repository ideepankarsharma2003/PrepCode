# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x= list(set([i for i in arr]))
    # print(x)
    x.sort()
    print(x[-2])
