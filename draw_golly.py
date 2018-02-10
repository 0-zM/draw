import sys
import golly

visual_execution = True #False for faster programs, True required for infinitely looping ones

file = golly.opendialog()
f = open(file).read()

golly.new("Executing " + file.split("/")[-1])
golly.setrule("B/S012345678")

golly.autoupdate(visual_execution)

commands = []

for line in f.splitlines():
	important = line.split("#")[0].strip()
	if not important:
		continue

	important = important.split()[0:5]
	commands.append((important[0], int(important[1]), int(important[2]), important[3], important[4]))

pointer = [0,0]
instruction_pointer = "start"

while True:
	command = commands[[i[0] for i in commands].index(instruction_pointer)]
	pointer = [
		pointer[0] + command[1],
		pointer[1] + command[2]
	]
	x = pointer[0]
	y = pointer[1]

	print(command, pointer)
	if golly.getcell(x, y):
		golly.fit()

		golly.exit()

	else:
		golly.setcell(x, y, 1)

	neighbours = [
		golly.getcell(x - 1, y),
		golly.getcell(x + 1, y),
		golly.getcell(x, y - 1),
		golly.getcell(x, y + 1),
	]

	if any(neighbours):
		instruction_pointer = command[3]

	else:
		instruction_pointer = command[4]

	#print(spaces)