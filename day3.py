line = None
with open('data/3') as f:
    line = f.readlines()[0]
# part 1
x, y = 0, 0
points = set()
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

# part 2
x, y = 0, 0
points = set()
isSanta = True
santa = (0, 0)
robo = (0, 0)
points.add(santa)
for c in line:
    x, y = 0, 0
    if isSanta:
        x, y = santa
    else:
        x, y = robo
    if c == '^':
        y -= 1
    elif c == 'v':
        y += 1
    elif c == '>':
        x += 1
    elif c == '<':
        x -= 1
    if isSanta:
        santa = (x, y)
        points.add(santa)
        isSanta = False
    else:
        robo = (x, y)
        points.add(robo)
        isSanta = True
print len(points)
