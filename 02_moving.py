fn = "inputs/02.txt"

aim = 0
x = 0
d = 0
with open(fn, 'r') as f:
	for line in f:
		cmd, v = line.split(" ")
		v = int(v)

		if cmd == "forward":
			x += v
			d += v*aim # remove for part 1
		if cmd == "down":
			# d += v # part 1
			aim += v 
		if cmd == "up":
			# d -= v # part 1
			aim -= v 

print(x*d)