def twoSum(numArray, targetNum):
	#Brute force approach
	if len(numArray) < 2:
		return -1, -1
	for indexOne in range(0, len(numArray) - 1):
		for indexTwo in range(indexOne + 1, len(numArray)):
			if numArray[indexOne] + numArray[indexTwo] == targetNum:
				return indexOne, indexTwo
	return -1, -1

def sortedTwoSum(numArray, targetNum):
	if len(numArray) < 2:
		return -1, -1
	indexOne = 0
	indexTwo = 1
	while indexOne < indexTwo:
		if numArray[indexOne] + numArray[indexTwo] == targetNum:
			return indexOne, indexTwo
		elif numArray[indexOne] + numArray[indexTwo] > targetNum:
			indexTwo -= 1
		else:
			indexOne += 1
			indexTwo = len(numArray) - 1
	return -1, -1

myArr = [0, 1, 2, 3, 4 ,5 ,6, 7, 8, 9, 10]
print sortedTwoSum(myArr, 13)