lines = []


while True:
	line = input("Enter sequence of lines: ")
	if line == '>':
		break
	lines.append(line.upper())

print(lines)