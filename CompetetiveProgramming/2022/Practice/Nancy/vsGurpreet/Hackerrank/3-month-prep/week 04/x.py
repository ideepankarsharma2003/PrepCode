def caesarCipher(s, k):
    # Write your code here
    sDash = ''
    l = [chr(x) for x in range(ord('a'), ord('z')+1)]
    lDash = l[k:]+l[:k]
    L = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    LDash = L[k:]+L[:k]

    for i in s:
        if i in l:
            index = l.index(i)
            sDash += lDash[index]
        elif i in L:
            index = L.index(i)
            sDash += LDash[index]
        else:
            sDash += i
    return sDash


str = 'middle-Outz'
print(caesarCipher(str, 2))