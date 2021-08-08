def organizingContainers(container):
	types = []
	no_balls = []
	n = len(container)
	for i in range(n):
		sum1 = 0
		for j in range(n):
			sum1 += container[i][j]
		types.append(sum1)
	for i in range(n):
		sum1 = 0
		for j in range(n):
			sum1+= container[j][i]
		no_balls.append(sum1)
	types.sort()
	no_balls.sort()
	print(types)
	print(no_balls)
	if types == no_balls:
		return "Possible"
	else:
		return "Impossible"
container = [[0,2,1], [1,1,1], [2,0,0]]
print(organizingContainers(container))