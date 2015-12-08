lines = []
floor = 0
with open('data/1') as f:
    lines = f.readlines()
line = lines[0]
for c in line:
    if c == '(':
        floor += 1
    else:
        floor -= 1
print floor
