# takes the existing latest interval [a, b] and a pair [x, y] and determines if pair overlaps [a, b]
def does_overlap(interval, pair):
    #pair [x, y] overlaps interval [a, b] if x <= b
    if pair[0] <= interval[1]:
        return True
    else:
        return False

def merge(interval, pair):
    if pair[1] >= interval[1]:
        interval = [interval[0], pair[1]]
    return interval

def find_intervals(overlapping):
    intervals = [overlapping[0]]
    for interval in overlapping:
        if does_overlap(intervals[-1], interval):  
            intervals[-1] = merge(intervals[-1], interval)
        else:
            intervals.append(interval)
    return intervals

if __name__ == "__main__":
    intervals = find_intervals([[1, 5], [3, 7], [6, 8], [5, 6], [10, 12], [11, 15]])
    print str(intervals)  

    intervals = find_intervals([[1, 3], [5, 6], [6, 8], [10, 12]])
    print str(intervals)  
