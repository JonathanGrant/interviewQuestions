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

##  O(n) runtime, O(1) space
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

def strstr(needle,haystack):
	return haystack.find(needle)

## O(n) runtime
def reverseWordsInString(myStr):
	wordStack = myStr.split()
	myStr = ""
	for word in range(0, len(wordStack)):
		myStr = myStr + wordStack.pop() + ' '
	return myStr

## O(n) time, O(1) space
def validNumber(myNumStr):
	stage = 0
	hadDecimalPoint = False
	for char in myNumStr:
		if stage == 0:
			if not char is ' ':
				stage = 1
		if stage == 1:
			if not char in ['+', '-']:
				stage = 2
		if stage == 2:
			if not char in ['0', '1', '2', '3', '4', '5' ,'6', '7', '8', '9']:
				if (not hadDecimalPoint) and char is '.':
					hadDecimalPoint = True
				else:
					stage = 3
		if stage == 3:
			if not char is ' ':
				return False
	return True

## O(n) time, O(1) space
def lengthOfLongestSubstring(myStr):
	charMap = []
	for i in range(0, 256):
		charMap.append(-1)
	i = 0
	maxLen = 0
	for j in range(0, len(myStr)):
		if charMap[ord(myStr[j])] >= i:
			i = charMap[ord(myStr[j])] + 1
		charMap[ord(myStr[j])] = j
		maxLen = max(j-i + 1, maxLen)
	return maxLen

print lengthOfLongestSubstring('dasfs5.02')
