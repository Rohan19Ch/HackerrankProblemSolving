def queensAttack(n, k, r_q, c_q, obstacles):
	s = set([(x,y) for y,x in obstacles])
	m = [
		[-1, 1],[0, 1],[1, 1],
		[-1, 0],       [1, 0],
		[-1,-1],[0,-1],[1,-1]
	]
	r = 0
	for d in m:
		y = r_q
		x = c_q
		while True:
			y += d[1]
			x += d[0]
			if x == 0 or y == 0 or x == n+1 or y == n+1:
				break
			if (x,y) in s:
				break
			r += 1
	return r
n = 5
k = 3
r_q = 4
c_q = 3
obstacles = [[5,5], [4,2], [2,3]]
print(queensAttack(n, k, r_q, c_q, obstacles))