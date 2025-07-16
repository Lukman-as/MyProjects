def max_interval_intersection(S):
    B = ([(left, 1) for left, right in S] + 
         [(right, -1) for left, right in S])
    B.sort()

    
    c = 0
    maxi = 0
    intervals = []
    start = None
    for x, d in B:
        prev_c = c
        c += d
        if c > maxi:
            maxi = c
            start = x
        elif c < maxi and prev_c == maxi:
            intervals.append((start, x))
            start = None
    print(maxi)
    return intervals

array = [(1,4), (2, 4), (1, 3), (2, 5), (6, 9)]
obj = max_interval_intersection(array)
print(obj)