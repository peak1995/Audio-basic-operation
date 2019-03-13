def linear_inter(alist, n):
    length = len(alist)
    new_lst = []
    if length == 0 or length == 1:
        print("Error")
        return

    for ii in range(1,length):
        diff = (alist[ii] - alist[ii-1]) / (n + 1)
        for jj in range(n + 1):
            new_lst.append(alist[ii-1] + jj * diff)
    new_lst.append(alist[-1])
    return new_lst

a = [0, 10, 15, 30]
print("1:", linear_inter(a, 1))
print("2:", linear_inter(a, 3))