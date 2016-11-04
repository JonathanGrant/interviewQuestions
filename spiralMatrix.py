# Given an n x m matrix, print it out in a spiral.

def printSpiral(matrix):
	topIndex = 0
	bottomIndex = len(matrix) - 1
	leftIndex = 0
	rightIndex = len(matrix[0]) - 1
	while topIndex < bottomIndex or leftIndex < rightIndex:
		print "top " + str(topIndex) + " bot " + str(bottomIndex) + " left " + str(leftIndex) + " right " + str(rightIndex)
		print "top"
		for i in range(leftIndex, rightIndex):
			print matrix[topIndex][i]
		print "right"
		for i in range(topIndex, bottomIndex):
			print matrix[i][rightIndex]
		print "bottom"
		for i in range(leftIndex, rightIndex):
			#print i, leftIndex, rightIndex
			print matrix[bottomIndex][len(matrix[0]) - 1 - i]
		print "left"
		if bottomIndex - topIndex > 1:
			for i in range(topIndex, bottomIndex):
				print matrix[len(matrix) - 1 - i][leftIndex]
		topIndex+=1
		bottomIndex-=1
		leftIndex+=1
		rightIndex-=1
myMatrix = [
[0,1,2,3,4,5],
[6,7,8,9,0,1],
[2,3,4,5,6,7],
[8,9,0,1,2,3],
[4,5,6,7,8,9]
]
printSpiral(myMatrix)