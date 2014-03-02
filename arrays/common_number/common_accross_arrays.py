def smallest_common(a, b, c):
    p1 = p2 = p3 = 0

    while p1 < len(a) and p2 < len(b) and p3 < len(c):

        # found the smallest number
        if a[p1] == b[p2] == c[p3]:
            return a[p1] 

        #advance the iterators
        #for the smallest value
        if a[p1] <= b[p2] and a[p1] <= c[p3]:
            p1 += 1
        elif b[p2] <= a[p1] and b[p2]<= c[p3]:
            p2 += 1
        elif c[p3] <= a[p1] and c[p3]<= b[p2]:
            p3 += 1

    return -1

if __name__ == "__main__":
    a1 = [6, 7, 10, 25, 30, 63, 64]
    a2 = [-1, 4, 5, 6, 7, 8, 50]
    a3 = [1, 6, 10, 14]
    print smallest_common(a1, a2, a3);

    a1 = [1, 7, 10, 25, 30, 63, 64]
    a2 = [-1, 4, 5, 6, 7, 8, 50]
    a3 = [1, 6, 10, 14]
    print smallest_common(a1, a2, a3);

    a1 = [6, 7, 9, 25, 30, 63, 64]
    a2 = [-1, 4, 5, 6, 7, 8, 9, 50]
    a3 = [1, 6, 9, 10, 14]
    print smallest_common(a1, a2, a3);


    a1 = [6, 7, 9, 25, 30, 63, 64]
    a2 = [-1, 4, 5, 6, 7, 8, 9, 50]
    a3 = [1, 9, 10, 14]
    print smallest_common(a1, a2, a3);