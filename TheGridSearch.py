def gridSearch(G, P):
	found = False
	for i in range(R-(r-1)):
		for j in range(C-(c-1)):
			if G[i][j]==P[0][0]:
				for m in range(r):
					for n in range(c):
						if P[m][n]!=G[i+m][j+n]:
							found = False
							break
						else:
							found= True
					if found==False:
						break
			if found == True:
				break
		if found == True:
			break

	if found==True:
		return 'YES'
	else:
		return 'NO'
g = ['7283455864', '6731158619', '8988242643', '3830589324', '2229505813', '5633845374', '6473530293', '7053106601', '0834282956', '4607924137']
p = ['9505', '3845', '3530']
gridSearch(g, p)