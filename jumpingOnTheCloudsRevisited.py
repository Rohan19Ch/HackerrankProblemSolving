def jumpingOnClouds(c, k):
	energy = 100
	length = len(c)
	index = k%length
	if c[index] == 0:
		energy -= 1
	else:
		energy -= 3
	while energy > 0 and index !=0:
		index = (index+k)%length
		if c[index] == 0:
			energy -= 1
		else:
			energy -= 3
	print(energy)
c = [0,0,1,0]
k = 2
jumpingOnClouds(c,k)