filename = "readFileDefault.py"

f = open(filename)
lines = []

for line in f:
    lines.append(line.strip())

print(lines)

