def check(arr):

    d= dict()
    for i in (arr):
        if i not in d:
            d[i]=1
        else:
            d[i]+=1

    # print(d)
    x= d.keys()
    lst1= []
    lst2= []
    for i in x:
        lst1.append(d[i])

    for i in lst1:
        if i not in lst2:
            lst2.append(i)
        else:
            return False
    
    return True



arr= [1, 2, 2, 1, 1, 3]
print((check(arr)))