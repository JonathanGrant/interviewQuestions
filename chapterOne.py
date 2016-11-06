def twoSum(numArray, targetNum):
	#Brute force approach
	if len(numArray) < 2:
		return -1, -1
	for indexOne in range(0, len(numArray) - 1):
		for indexTwo in range(indexOne + 1, len(numArray)):
			if numArray[indexOne] + numArray[indexTwo] == targetNum:
				return indexOne, indexTwo
	return -1, -1

myArr = [0, 1, 2, 3, 4 ,5 ,6, 7, 8, 9, 10]
print twoSum(myArr, 13)