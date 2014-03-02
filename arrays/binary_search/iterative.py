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
	index = search([1, 2, 3, 5, 7, 9], 2)
	print index


