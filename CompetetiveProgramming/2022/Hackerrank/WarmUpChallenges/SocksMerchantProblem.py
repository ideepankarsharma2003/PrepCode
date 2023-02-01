n=9
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]

pairs=0
s=set()
for i in arr:
    if i in s:
        s.remove(i)
        pairs+=1
    else:
        s.add(i)

print(pairs)
