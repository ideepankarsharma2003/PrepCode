def fibonacciModified(t1, t2, n):
    # Write your code here
    f = t1
    s = t2
    t = 0
    for i in range(n-2):
        t = f + s**2
        # print(t)
        f = s
        s = t
        # n = n-1
    return t
