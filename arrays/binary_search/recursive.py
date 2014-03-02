def search(array, low, high, key):
    if low > high:
        return -1

    mid = low + ((high - low) /2)

    if key == array[mid]:
        return mid

    # take the first half or the second half of the array?

    if key < array[mid]: #take the first half of the array
        return search(array, low, mid-1, key)
    else:
        return search(array, mid+1, high, key)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 6, 21, 78, 101, 768]
    print "Searching through" + str(a) + " for 2"
    print search(a, 0, len(a)-1, 2)

    print "Searching through" + str(a) + " for 6"
    print search(a, 0, len(a)-1, 6)

    print "Searching through" + str(a) + " for 22"
    print search(a, 0, len(a)-1, 22)

    print "Searching through" + str(a) + " for 78"
    print search(a, 0, len(a)-1, 78)


