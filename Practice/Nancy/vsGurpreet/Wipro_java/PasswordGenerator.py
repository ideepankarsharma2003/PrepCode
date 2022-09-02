def check_stable(num):
    num= str(num)
    d= {}

    for i in num:
        if i not in d.keys():
            d[i]= 1
        else:
            d[i]+= 1 

    # print(d)
    x = num[0]
    x = d[x]
    for i in d.values():
        if i!=x:
            return False
    return True




def password_generator(a, b, c, d, e):
    arr= [a, b, c, d, e]
    ns=0 # count of stable
    nu=0 # count of unstable

    for i in arr:
        if check_stable(i):
            ns+=1
        else:
            nu+=1

    return (ns*10)+nu



password= password_generator(12, 1313, 122, 678, 898)
print(password)