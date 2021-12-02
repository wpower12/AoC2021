fn = "inputs/01.txt"

nums = []
with open(fn, 'r') as f:
	for line in f:
		i = int(line)
		nums.append(i)

triples = []

for i in range(2, len(nums)):
	triples.append(nums[i-2]+nums[i-1]+nums[i])

# this used to be part 1, but I made it operate over triples, instead.
count = 0
last = -1
for i in triples:
	if last == -1:
		last = i
		continue

	if i > last:
		count += 1

	last = i

print(count)