## Problems are from Leetcode interview prep

## O(n^2) time, O(1) space
def twoSum(numArray, targetNum):
	#Brute force approach
	if len(numArray) < 2:
		return -1, -1
	for indexOne in range(0, len(numArray) - 1):
		for indexTwo in range(indexOne + 1, len(numArray)):
			if numArray[indexOne] + numArray[indexTwo] == targetNum:
				return indexOne, indexTwo
	return -1, -1

## O(n) time, O(1) space
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

def validPalindrome(myStr):
	simpleStr = ''.join(myStr.lower().split())
	indexOne = 0
	indexTwo = len(simpleStr) - 1
	while indexOne < indexTwo:
		if simpleStr[indexOne] != simpleStr[indexTwo]:
			return False
		indexOne += 1
		indexTwo -= 1
	return True

print validPalindrome('not a valid palindrome')