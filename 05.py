fn = "inputs/05.txt"

with open(fn) as f:
	lines = f.readlines()

line_segs = []
max_x, max_y = 0, 0

for line in lines:
	s_str, _, e_str = line.strip("\n").split(" ")
	# print(line.strip("\n").split(" "))
	x_0, y_0 = list(map(lambda x: int(x), s_str.split(",")))
	x_1, y_1 = list(map(lambda x: int(x), e_str.split(",")))

	line_segs.append([(x_0, y_0), (x_1, y_1)])
	if x_0 > max_x: max_x = x_0
	if x_1 > max_x: max_x = x_1
	if y_0 > max_y: max_y = y_0
	if y_1 > max_y: max_y = y_1

print(max_x, max_y)

terrain = [[0 for _ in range(991)] for _ in range(991)]

for (x_0, y_0), (x_1, y_1) in line_segs:
	
	if x_0 == x_1:
		# Vertical
		if y_1 > y_0:
			for j in range(y_0, y_1+1):
				terrain[x_0][j] += 1
		else:
			for j in range(y_1, y_0+1):
				terrain[x_0][j] += 1
	elif y_0 == y_1:
		# Horizontal
		if x_1 > x_0:
			for i in range(x_0, x_1+1):
				terrain[i][y_0] += 1
		else:
			for i in range(x_1, x_0+1):
				terrain[i][y_0] += 1

	else:
		# Diagonal
		if x_1 > x_0:
			x_vals = range(x_0, x_1)
		else:
			x_vals = range(x_1, x_0)

		if y_1 > y_0:
			y_vals = range(y_0, y_1)
		else:
			y_vals = range(y_1, y_0)

		for p_x, p_y in zip(x_vals, y_vals):
			terrain[p_x][p_y] += 1

# print(terrain)
count = 0
for i in range(991):
	for j in range(991):
		if terrain[i][j] >= 2:
			count += 1

print(count)