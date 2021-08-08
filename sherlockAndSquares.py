import math
def squares(a, b):
	return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1
print(squares(24, 49))