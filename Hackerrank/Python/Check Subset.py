# www.hackerrank.com/challenges/py-check-subset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for _ in range(T):
    nA = int(input())
    A = set(map(int, input().split()))
    nB = int(input())
    B = set(map(int, input().split()))

    # print(f'A= {A}')
    # print(f'B= {B}')

    print(A.issubset(B))
