fn = "inputs/08.txt"

with open(fn) as f:
	lines = f.readlines()


four_segs = list(map(lambda x: x.split(" | ")[1].strip("\n").split(" "), lines))

count = 0
ex_count = 0
for ex in four_segs:
	seen = False
	for seg in ex:
		if len(seg) in [2, 3, 4, 7]:
			count += 1
			seen = True
	if seen:
		ex_count += 1

print(ex_count, len(four_segs))