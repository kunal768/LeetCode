def flipAndInvertImage(A):
	return [list(map(lambda x : x ^ 1 , lis[::-1])) for lis in A ]
	


print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))	