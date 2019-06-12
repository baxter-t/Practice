def lcs(x, y):

	currentSub = ""
	currentBest = ""

	for i in range(len(x)):
		for j in range(i + len(currentBest), len(x)):
			currentSub = x[i:j+1]
			if currentSub in y and len(currentSub) > len(currentBest):
				currentBest = currentSub


	return currentBest

print(lcs("abcdefgh", "abfgh"))
