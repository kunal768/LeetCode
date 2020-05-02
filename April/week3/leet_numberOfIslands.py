# Nick white you're a hero boss

def BFS(grid,i,j,row,col):
	# break condition
	if(i<0 or j <0 or i>=row or j >= col or grid[i][j] == '0') :
		return 
	grid[i][j] = '0'
	BFS(grid,i-1,j,row,col) #up
	BFS(grid,i+1,j,row,col) #down
	BFS(grid,i,j+1,row,col) #left
	BFS(grid,i,j-1,row,col) #right


def numIslands(grid):
	if len(grid) == 0:
		return 0
	row = len(grid)
	col = len(grid[0])
	count = 0
	for i in range(row):
		for j in range(col) :
			if grid[i][j] == '1' :
				count += 1
				BFS(grid,i,j)
	return count



