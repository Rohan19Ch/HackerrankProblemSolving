def pageCount(n, p):
	if n%2 !=0:
		if p <= n//2:
			turns = p//2
		else:
			turns = (n-p)//2
	else:
		if p <= n//2:
			turns = p//2
		else:
			turns = 0
			start = n
			while start > p:
				turns += 1
				start-=2 
	return turns
n = 6
p = 5
print(pageCount(n,p))