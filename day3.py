line = None
points = set()
x, y = 0, 0
with open('data/3') as f:
    line = f.readlines()[0]
for c in line:
    points.add((x, y))
    if c == '^':
        y -= 1
    elif c == 'v':
        y += 1
    elif c == '>':
        x += 1
    elif c == '<':
        x -= 1
print len(points)
