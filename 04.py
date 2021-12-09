fn = "inputs/04.txt"


with open(fn) as f:

	draws = list(map(lambda x: int(x), f.readline().strip("\n").split(",")))

	print(draws)
	board_vals  = []
	board_states = []

	lines = f.readlines()
	num_boards = int((len(lines))/6)
	print(num_boards)

for i in range(num_boards):
	new_board = []
	os = i*6
	for j in range(5):
		line = lines[j+os+1].strip("\n")
		vals = line.split(" ")
		while "" in vals:
			vals.remove("")
		vals = list(map(lambda x: int(x), vals))
		new_board.append(vals)
	new_state = [[False, False, False, False, False],
				[False, False, False, False, False],
				[False, False, False, False, False],
				[False, False, False, False, False],
				[False, False, False, False, False]]

	board_vals.append(new_board)
	board_states.append(new_state)


def calc_score(vals, state, draw):
	sum_um = 0
	for i in range(5):
		for j in range(5):
			if not state[i][j]:
				sum_um += vals[i][j]
	return draw*sum_um

dones = [False for i in range(num_boards)]

done = False
for d in draws:
	for b in range(num_boards):

		if dones[b]:
			continue
			
		board = board_vals[b]

		# Change state for new val
		check_state = False
		for i in range(5):
			for j in range(5):
				if board[i][j] == d:
					board_states[b][i][j] = True
					check_state = True

		board = board_states[b]
		if check_state:
			# check columns
			for i in range(5):
				test = board[i][0] & board[i][1] & board[i][2] & board[i][3] & board[i][4]
				if test:
					print("Win!!")
					print(calc_score(board_vals[b], board_states[b], d))
					dones[b] = True
					done = True
					break

			# rows
			for i in range(5):
				test = board[0][i] & board[1][i] & board[2][i] & board[3][i] & board[4][i]
				if test:
					print("Win!!")
					print(calc_score(board_vals[b], board_states[b], d))
					dones[b] = True
					done = True
					break

	# if done:
	# 	break


