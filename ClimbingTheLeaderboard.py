def climbingLeaderboard(ranked, player):
	setRanked = []	
	for i in ranked:
		if i not in setRanked:
			setRanked.append(i)
	player.sort(reverse = True)
	rankList = []
	j = 0
	for i in range(len(player)):
		while j<len(setRanked) and player[i]<setRanked[j]:
			j+=1
		rank = j+1
		rankList.append(rank)
		newList = rankList[::-1]
	return newList
ranked = [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]
print(climbingLeaderboard(ranked, player))