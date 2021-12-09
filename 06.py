fn = "inputs/06.txt"
num_days = 256

with open(fn) as f:
	line = f.readline()

fish = list(map(lambda x: int(x), line.strip("\n").split(",")))

print(fish)

for d in range(num_days):

	new_fish = []
	for f in range(len(fish)):

		if fish[f] == 0:
			fish.append(8)
			fish[f] = 6
			# print("hi")
		else:
			fish[f] -= 1

print(len(fish))
		
