
def minTimeToVisitAllPoints(points):
	n = len(points)
	summ = 0     
	for i in range(n-1):
		print(points[i],points[i+1])
		summ += max(abs(points[i+1][0] - points[i][0]),abs(points[i+1][1]-points[i][1]))
	return summ



minTimeToVisitAllPoints([[3,2],[-2,2]])