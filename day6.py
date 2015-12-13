lines = []
grid = {}
with open('data/6') as f:
    lines = f.readlines()
def setup(line):
    if len(line.split()) == 5:
        _, action, start, _, end = line.split()
    else:
        action, start, _, end = line.split()
    start = map(int, start.split(','))
    end = map(int, end.split(','))
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            if action == 'on':
                grid.setdefault(x, {})[y] = True
            elif action == 'off':
                grid.setdefault(x, {})[y] = False
            else:
                grid.setdefault(x, {})[y] = not grid.setdefault(x, {}).get(y, 0)
for line in lines:
    setup(line)
count = 0
for x in grid.values():
    for y in x.values():
        if y:
            count += 1
print count

