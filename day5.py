lines = []
with open("data/5") as f:
    lines = f.readlines()

# part 1
vowels = 'aeiou'
bads = ['ab', 'cd', 'pq', 'xy']
nices = 0
for line in lines:
    vowel = 0
    twice = False
    bad = False
    prev = None
    for c in line.strip():
        if c in vowels:
            vowel += 1
        if prev:
            if (prev + c) in bads:
                bad = True
                break
            if prev == c:
                twice = True
        prev = c
    if vowel > 2 and twice and not bad:
        nices += 1
print nices


# part 2
def nice(line):
    twice = False
    have_triple = False
    variant1 = zip(line[::2], line[1::2])
    variant2 = zip(line[1::2], line[2::2])
    for i, v in enumerate(variant2):
        variant1.insert(2*i+1, v)
    for i, item in enumerate(variant1):
        if item in variant1[i+2:]:
            twice = True
            break
    triple = zip(line[::3], line[1::3], line[2::3])
    triple += zip(line[1::3], line[2::3], line[3::3])
    triple += zip(line[2::3], line[3::3], line[4::3])
    for item in triple:
        if item[0] == item[2]:
            have_triple = True
            break
    if have_triple and twice:
        return True
    return False
count = 0
for line in lines:
    if nice(line):
        count += 1
print count
