def search(array, key):
	low = 0
	high = len(array)-1
	
	while low <= high:
		mid = low + ((high - low)/2)

		if array[mid] == key:
			return mid
		
		#move the low or the high pointer?

		if key < array[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return -1

if __name__ == "__main__":
	a = [1, 2, 3, 6, 8, 19, 20, 23, 42, 67, 91]
	print "Searching through" + str(a) + " for 2"
	index = search(a, 2)
	print index

	print "Searching through" + str(a) + " for 9"
	index = search(a, 9)
	print index

	print "Searching through" + str(a) + " for 23"
	index = search(a, 23)
	print index

	print "Searching through" + str(a) + " for 101"
	index = search(a, 101)
	print index

