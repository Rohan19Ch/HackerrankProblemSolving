import math
def extraLongFactorials(n):
	if n == 1:
		return 1
	else:
		return n*extraLongFactorials(n-1)
print(extraLongFactorials(25))