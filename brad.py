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

def mergeTwoSortedArrays(arr1, arr2):
	lenArr1 = len(arr1)
	lenArr2 = len(arr2)
	i = 0
	j = 0
	while j < lenArr2 and i < len(arr1):
		if arr1[i] < arr2[j]:
			i += 1
		else:
			arr1.insert(i, arr2[j])
			j += 1
	if len(arr1) < lenArr1 + lenArr2:
		while j < lenArr2:
			arr1.append(arr2[j])
			j += 1
	return arr1

def sortFromOrder(order, string):
	orderList = [0] * 26
	# Assuming all lowercase letters
	for char in string:
		orderList[ord(char) - 97] += 1
	realStringArr = []
	for char in order:
		realStringArr.extend([char] * orderList[ord(char) - 97])
	return ''.join(realStringArr)

def twoSum(arr, theSum):
	arr.sort()
	low = 0
	high = len(arr) - 1
	while low < high:
		tempSum = arr[low] + arr[high]
		if tempSum == theSum:
			return arr[low], arr[high]
		elif tempSum > theSum:
			high -= 1
		else:
			low += 1
	return 'Cannot find the sum'

def isPalin(myStr):
	start = 0
	lenStr = len(myStr)
	end = lenStr - 1
	while start < end:
		while start < lenStr - 1 and not myStr[start].isalpha():
			start += 1
		while end > 0 and not myStr[end].isalpha():
			end -= 1
		if start > end:
			return True
		elif myStr[start].lower() != myStr[end].lower():
			return False
		start += 1
		end -= 1
	return True

def printAllOrders(decided, undecided):
	if len(undecided) == 1:
		print ' '.join(decided + undecided)
	else:
		for i in range(0, len(undecided)):
			printAllOrders(decided + [undecided[i]], [x for x in undecided if x != undecided[i]])

def printAllOrdersNSelections(decided, undecided, numSelections):
	if len(decided) == numSelections - 1 or len(undecided) == 1:
		mainStr = ' '.join(decided)
		for num in undecided:
			print mainStr + ' ' + str(num)
	else:
		for i in range(0, len(undecided)):
			printAllOrdersNSelections(decided + [undecided[i]], [x for x in undecided if x != undecided[i]], numSelections)

printAllOrdersNSelections([], ['3', '5', '7', '9'], 2)