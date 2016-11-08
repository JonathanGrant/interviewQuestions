# There are unlimited of each type of cake
# Each cake has a weight (kg) and a value (british pounds) (int, int)
# I have a bag that can hold a limited amount of weight, and I want to get the most value
# O(n * k) time, O(1) space where n is num cakes and k is bag capacity
def maxValueFromCakes(bagCapacity, cakes):
	totalCakeMoney = 0
	while bagCapacity > 0:
		maxCakeValue = 0
		maxCakePrice = 0
		maxCakeWeight = 0
		for weight, value in cakes:
			if weight <= bagCapacity:
				if weight < 0 and value > 0:
					return float('inf')
				elif weight < 0 and value < 0:
					continue
				if (1.0 * value) / weight > maxCakeValue:
					maxCakeValue = (1.0 * value) / weight
					maxCakePrice = value
					maxCakeWeight = weight
		if maxCakeValue is 0:
			break
		totalCakeMoney += maxCakePrice
		bagCapacity -= maxCakeWeight
	return totalCakeMoney

cakes = [[-7, -160], [3, 90], [2, 15]]
bagCapacity = 20
print maxValueFromCakes(bagCapacity, cakes)