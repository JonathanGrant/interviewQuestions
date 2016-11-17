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

recursePrint(1239456)
recursePrint(0)
iterPrint(1239456)
iterPrint(0)