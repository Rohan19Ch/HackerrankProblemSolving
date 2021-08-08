import math
def encryption(s):
	l = list(s.split())
	print(l)
	s = ""
	s = s.join(l)
	print(s)
	length = len(s)
	print(length)
	floor = math.floor(math.sqrt(length))
	ceil = math.ceil(math.sqrt(length))
	print(floor, ceil)
	areas = [[floor,floor], [floor,ceil], [ceil,ceil]]
	for i in areas:
		if i[0]*i[1]>=length:
			break
	print(i)
	finalGrid = []
	k = 0
	while k<length:
		finalGrid.append(s[k:k+i[1]])
		print(finalGrid)
		k = k+i[1]
	print(finalGrid)
	height = i[0]
	width = i[1]
	newGrid = []
	for i in range(width):
		string = ""
		for j in range(height):
			try:
				x = finalGrid[j][i]
				print(x)
				string = string + x
			except IndexError:
				continue
		newGrid.append(string)
	print(newGrid)
	returnString = ""
	for i in newGrid:
		returnString = returnString + i
		returnString += " "
	return returnString
s = "if man was meant to stay on the ground god would have given us roots"
#s = "chillout"
print(encryption(s))