# www.hackerrank.com/challenges/py-check-strict-superset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
def checkStrictSuperset(A, n):
    for i in range(n):
        X = set(map(int, input().split()))
        # print(f'X= {X}')
        if not (A.issuperset(X) and A != X):
            return False
    return True


A = set(map(int, input().split()))
n = int(input())
# print(f'A= {A}')

print(checkStrictSuperset(A, n))
