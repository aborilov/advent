lines = []
floor = 0
with open('data/1') as f:
    lines = f.readlines()
line = lines[0]
count = 1
basement = 0
for c in line:
    if c == '(':
        floor += 1
    else:
        floor -= 1
    if not basement and floor == -1:
        basement = count
    else:
        count += 1
print floor
print basement
