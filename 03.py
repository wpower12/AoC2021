fn = "inputs/03.txt"
N = 12
# 010 100 000 110

# o_counts = [0 for i in range(N)]
# z_counts = [0 for i in range(N)]
# with open(fn, 'r') as f:
# 	for line in f:
# 		v = int(line)
# 		for i in range(N):
# 			if 2**i & v > 0:
# 				o_counts[i] += 1
# 			else:
# 				z_counts[i] += 1

# print(o_counts)
# print(z_counts)

# gamma   = 0
# epsilon = 0
# for i in range(N):
# 	if o_counts[i] > z_counts[i]:
# 		gamma += 2**i
# 	elif z_counts[i] > o_counts[i]:
# 		epsilon += 2**i
# 	else:
# 		print("oh.")

# print(gamma, epsilon)
# print(gamma*epsilon)

from collections import Counter

with open(fn) as f:
    inp = [line.strip() for line in f.readlines()]

# part 1
most, least = "", ""
for col in range(len(inp[0])):
    out = Counter([line[col] for line in inp])
    if out["1"] > out["0"]:
        most += "1"
        least += "0"
    else:
        most += "0"
        least += "1"

print(int(most, 2) * int(least, 2))
