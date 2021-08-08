def detonate(l1, r, c):
	retList = [["O"]*c for i in range(r)]
	for i in range(r):
		for j in range(c):
			if l1[i][j] == "O":
				retList[i][j]='.'
				if(i-1 >= 0):retList[i-1][j]='.'
				if(i+1 < r):retList[i+1][j]='.'
				if(j-1 >= 0):retList[i][j-1]='.'
				if(j+1 < c):retList[i][j+1]='.'
	return retList
def bomberMan(n, grid):
	r = len(grid)
	c = len(grid[0])
	newList = [[i for i in grid[j]] for j in range(r)]
	if n in [0,1]:
		return grid
	elif n%2 == 0:
		return ['O'*c for j in range(r)]
	else:
		if n%4 == 3:
			list2 = detonate(newList, r, c)
			retString = []
			for i in list2:
				retString.append("".join(i))
			return retString
		elif n != 1:
			list2 = detonate(newList, r, c)
			print(list2)
			list3 = detonate(list2, r, c)
			print(list3)
			retString = []
			for i in list3:
				retString.append("".join(i))
			return retString
n = 2
grid =[".....", ".....", ".....", ".....", ".....", "....."]
answer = bomberMan(n, grid)
print(answer)