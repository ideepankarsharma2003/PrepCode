k = -1
for i in range(1, 7):
    if i != 6:
        for j in range(6-i+1):
            print(end=' ')
        print(end='*')
        print((k)*' ', end='')
        k += 2
        if i > 1:
            print(end='*')
    else:
        for j in range(i):
            print(end='* ')

    print()
