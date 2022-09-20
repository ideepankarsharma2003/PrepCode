n= 6
c = [0, 0, 0, 0, 1, 0]

jump=0
i=0

while i< (n-1):
    if (i+2) >= (n) or c[i+2] == 1:
        jump+=1
        i+=1
    else:
        jump += 1
        i+=2
print(jump)
