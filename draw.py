import sys
import golly

f = open(sys.argv[1]).read()

commands = []

for line in f.splitlines():
	important = line.split("#")[0].strip()
	if not important:
		continue

	important = important.split()[0:5]
	commands.append((important[0], int(important[1]), int(important[2]), important[3], important[4]))

spaces = {}
pointer = [0,0]
instruction_pointer = "start"

while True:
	command = commands[[i[0] for i in commands].index(instruction_pointer)]
	pointer = [
		pointer[0] + command[1],
		pointer[1] + command[2]
	]
	print(command, pointer)
	if spaces.get(tuple(pointer), None):
		break

	else:
		spaces[tuple(pointer)] = True

	neighbours = [
		spaces.get(tuple([pointer[i] + [-1, 0][i] for i in [0,1]])),
		spaces.get(tuple([pointer[i] + [1, 0][i] for i in [0,1]])),
		spaces.get(tuple([pointer[i] + [0, -1][i] for i in [0,1]])),
		spaces.get(tuple([pointer[i] + [0, 1][i] for i in [0,1]])),
	]

	if any(neighbours):
		instruction_pointer = command[3]

	else:
		instruction_pointer = command[4]

	#print(spaces)
print(len(spaces))