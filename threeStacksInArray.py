class ThreeStack:
	def __init__(self):
		self.stackArr = []
		for i in range(0, 98):
			self.stackArr.append(0)

	def push(self, stackNum, data):
		lenMyStack = self.stackArr[stackNum]
		indexNewTop = lenMyStack * 3 + stackNum + 3
		self.stackArr[indexNewTop] = data
		self.stackArr[stackNum] += 1

	def pop(self, stackNum):
		lenMyStack = self.stackArr[stackNum]
		indexOldTop = lenMyStack * 3 + stackNum
		if indexOldTop < 3:
			return 0
		numToReturn = self.stackArr[indexOldTop]
		self.stackArr[indexOldTop] = 0
		self.stackArr[stackNum] -= 1
		return numToReturn

stackOne = [0, 1, 2, 3, 4, 5]
stackTwo = [6, 7, 8, 9, 10, 11]
stackThree = [12, 13, 14, 15, 16, 17]

myThreeStack = ThreeStack()
for i in range(0, len(stackOne)):
	myThreeStack.push(0, stackOne[i])
	myThreeStack.push(1, stackTwo[i])
	myThreeStack.push(2, stackThree[i])

print myThreeStack.pop(0)
print myThreeStack.pop(0)
print myThreeStack.pop(1)
print myThreeStack.pop(2)