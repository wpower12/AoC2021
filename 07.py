fn = "inputs/07.txt"

with open(fn) as f:
	vals = list(map(lambda x: int(x), f.readline().split(",")))

# print(vals)
print(max(vals))


def calc_cost(idx, vals):
	cost = 0
	for v in vals:
		cost += abs(idx-v)
	return cost


def calc_cost_2(idx, vals):
	cost = 0
	for v in vals:
		c = abs(idx-v)
		cost += (c*(c+1)/2)
	return cost


best_idx  = 0
best_cost = calc_cost_2(0, vals)

for i in range(1, max(vals)):
	c = calc_cost_2(i, vals)

	if c < best_cost:
		best_idx  = i
		best_cost = c 

print(best_cost)

