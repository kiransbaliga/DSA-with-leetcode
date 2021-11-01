class Solution:
    def solve(self, board: List[List[str]]) -> None:
	    n, m = len(board), len(board[0])

	# nothing to do, all cells are on the edges
	    if n<3 or m<3:            
		    return

	    def check(i, j):
		    """ Mark all reachable Os from (i, j) as 1 """
		    tocheck = {(i, j)}
		    while tocheck:
			    i, j = tocheck.pop()
			    board[i][j] = 1
			    tocheck.update([(r, c) for r, c in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)) if 0<=r<n and 0<=c<m and board[r][c]=='O'])

	# Check left and right edges of the board
	    for i, row in enumerate(board):
		    if row[0] == 'O':
			    check(i, 0)
		    if row[m-1] == 'O':
			    check(i, m-1)

	# Check top and bottom edges of the board (excluding corners)
	    for j in range(1, m - 1):
		    if board[0][j] == 'O':
			    check(0, j)
		    if board[n-1][j] == 'O':
			    check(n-1, j)

	# Iterate through the board, flip all 'O' cells to 'X' and revert 1 cells to 'O'
	    for row in board:
		    for j, cell in enumerate(row):
			    if cell == 'O':
				    row[j] = 'X'
			    elif cell == 1:
				    row[j] = 'O'