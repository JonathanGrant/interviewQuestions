# Given an n x m matrix, Rotate it x-times clockwise.

def rotate(matrix, numRotations):
	if numRotations is 0:
		return matrix
	topCount = 0
	bottomCount = len(matrix) - 1
	leftCount = 0
	rightCount = len(matrix) - 1
	while numRotations > 0:
		while(topCount < bottomCount or leftCount < rightCount):
			for index in range(topCount, bottomCount):
				temp = matrix[topCount][index]
				matrix[topCount][index] = matrix[index][rightCount]
				matrix[index][rightCount] = matrix[bottomCount][len(matrix) - 1 - index]
				matrix[bottomCount][len(matrix) - 1 - index] = matrix[len(matrix) - 1 - index][leftCount]
				matrix[len(matrix) - 1 - index][leftCount] = temp
			topCount += 1
			leftCount += 1
			bottomCount-= 1
			rightCount -= 1
		numRotations -= 1
	return matrix

myMatrix = [
[0,1,2,3,4,5],
[6,7,8,9,0,1],
[2,3,4,5,6,7],
[8,9,0,1,2,3],
[4,5,6,7,8,9],
[9,8,7,6,5,4]
]
for row in rotate(myMatrix, 1):
	print row