def utopianTree(n):
	height = 1
	for i in range(1,n+1):
		if i%2 == 0:
			height+=1
		elif i%2 != 0:
			height =height*2
	return height
print(utopianTree(4))