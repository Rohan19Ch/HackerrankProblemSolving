def permutationEquation(p):
	x = [0 for i in range(len(p))]
	print(x)
	for i in p:
		print(i)
		x[p[p[i-1]-1]-1] = i
	print(x)
p = [5,2,1,3,4]
permutationEquation(p)