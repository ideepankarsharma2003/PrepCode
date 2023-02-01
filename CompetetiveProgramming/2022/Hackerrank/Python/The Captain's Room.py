# www.hackerrank.com/challenges/py-the-captains-room/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

K= int(input())
rooms= list(map(int, input().split()))

d= dict()

for i in rooms:
    if i not in d.keys():
        d[i]= 1
    else:
        d[i]+=1

for i in d.keys():
    if d[i]!=K:
        print(i)