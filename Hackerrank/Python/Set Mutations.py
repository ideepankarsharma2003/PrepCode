# https://www.hackerrank.com/challenges/py-set-mutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

S= int(input())
A = set(map(int, input().split()))

N= int(input())

operation= []
B= ()

for i in range(N):
    
    operation= list(map(str, input().split()))
    # operation[1]= int(operation[1]) # NO NEED !!
    # print(f'Operation= {operation}')

    B= set(map(int, input().split()))
    # print(f'B= {B}')
        
    if operation[0]=='intersection_update':
        A.intersection_update(B)
    elif operation[0]=='update':
        A.update(B)
    elif operation[0]=='symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif operation[0]=='difference_update':
        A.difference_update(B)
    
print(sum(A))

