def getMoneySpent(keyboards, drives, b):
	max = -1
	for i in keyboards:
		for j in drives:
			if i+j > max and i+j <=b:
				max = i+j
	return max
keyboards = [4]
USBs = [5]
Budget = 5
print(getMoneySpent(keyboards, USBs, Budget))