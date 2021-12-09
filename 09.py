fn = "inputs/09.txt"

grid = []
with open(fn) as f:
	for line in f.readlines():
		new_vals = []
		for c in line.strip("\n"):
			new_vals.append(int(c))
		grid.append(new_vals)

X = len(grid[0])
Y = len(grid)


def is_min(i, j):
	N, S, E, W = 10, 10, 10, 10

	if i-1 >= 0:
		W = grid[j][i-1]
	if i+1 < X:
		E = grid[j][i+1]

	if j-1 >= 0:
		S = grid[j-1][i]
	if j+1 < Y:
		N = grid[j+1][i]

	v = grid[j][i]
	return (v < N and v < E and v < S and v < W)


# BFS till you hit 9's
def basin_size(i, j):
	seen = [[False for _ in range(X)] for _ in range(Y)]
	queue = []
	queue.append((i,j))
	b_size = 0
	seen[j][i] = True	
	while len(queue) > 0:
		x, y = queue.pop()
		b_size += 1
		for n_x, n_y in neighbors(x, y):
			if grid[n_y][n_x] < 9 and not seen[n_y][n_x]:
				queue.append((n_x, n_y))
				seen[n_y][n_x] = True
	return b_size


def neighbors(i, j):
	ns = []
	if i-1 >= 0:
		ns.append((i-1, j))
	if i+1 < X:
		ns.append((i+1, j))
	if j-1 >= 0:
		ns.append((i, j-1))
	if j+1 < Y:
		ns.append((i, j+1))
	return ns


sum_risk = 0
basin_sizes = []
for i in range(X):
	for j in range(Y):

		if is_min(i, j):
			sum_risk += (1+grid[j][i])
			basin_sizes.append(basin_size(i, j))

print("sum_risks: ", sum_risk)
sorted_b_sizes = sorted(basin_sizes)
print(sorted_b_sizes[-1]*sorted_b_sizes[-2]*sorted_b_sizes[-3])