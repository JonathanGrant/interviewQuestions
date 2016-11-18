def needleInHaystack(haystack, needle):
	haystackLen = len(haystack)
	needleLen = len(needle)
	if needleLen > haystackLen:
		return False
	needlePoint = 0
	for hayPoint in range(0, haystackLen):
		while(haystack[hayPoint] == needle[needlePoint]):
			hayPoint += 1
			needlePoint += 1
			if needlePoint >= needleLen:
				return True
			if hayPoint >= haystackLen:
				return False
		hayPoint -= needlePoint
		needlePoint = 0
	return False

def recursePrint(num):
	print (num % 10)
	if num > 9:
		recursePrint(num / 10)

def iterPrint(num):
	while num > 9:
		print (num % 10)
		num = num / 10
	print num

def printPrimes(num):
	if num > 1:
		if num % 2 == 0:
			print 2
			printPrimes(num / 2)
		else:
			div = 3
			while num % div != 0:
				div += 2
				if div > num:
					div = num
					break
			print div
			printPrimes(num / div)

def maxAdjacentSum(arr):
	arrLen = len(arr)
	if arrLen == 0:
		return -999999
	if arrLen == 1:
		return arr[0]
	maxAdd = -999999
	curSum = 0
	for num in arr:
		curSum += num
		maxAdd = max(curSum, maxAdd)
	return max(maxAdd, maxAdjacentSum(arr[1:]))

def BinarySearch(arr, num, add):
	arrLen = len(arr)
	if arrLen == 0:
		return -1
	if arrLen == 1:
		if arr[0] == num:
			return add
	mid = arr[arrLen/2]
	if num == mid:
		return (arrLen / 2) + add
	elif num < mid:
		return BinarySearch(arr[0:arrLen/2 - 1], num, add)
	else:
		return BinarySearch(arr[arrLen/2:], num, add + arrLen / 2)

def swappedBS(arr, num):
	arrLen = len(arr)
	if arrLen == 0:
		return -1
	if arrLen == 1:
		if arr[0] == num:
			return 0
		else:
			return -1
	elif arrLen == 2:
		for i in range(0, 2):
			if arr[i] == num:
				return i
		return -1
	else:
		mid = arrLen / 2
		if num == arr[mid]:
			return mid
		elif num < arr[mid]:
			return BinarySearch(arr[mid:], num, mid)
		else:
			return BinarySearch(arr[:mid-1], num, 0)

def convertIsland(arr, m, n, x, y):
	if arr[y][x] == 1:
		arr[y][x] = 0
		if y < n - 1:
			convertIsland(arr, m, n, x, y + 1)
		if y > 0:
			convertIsland(arr, m, n, x, y - 1)
		if x < m - 1:
			convertIsland(arr, m, n, x + 1, y)
		if x > 0:
			convertIsland(arr, m, n, x - 1, y)

def countIslands(arr, m, n):
	total = 0
	for y in range(0, n):
		for x in range(0, m):
			if arr[y][x] == 1:
				total += 1
				convertIsland(arr, m, n, x, y)
	return total

myMap = [
[0, 0, 0, 1, 1],
[0, 1, 0, 0, 0],
[0, 0, 0, 1, 0],
[1, 1, 0, 1, 0],
[1, 1, 0, 1, 0]]
print countIslands(myMap, 5, 5)