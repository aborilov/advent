lines = []
vowels = 'aeiou'
bads = ['ab', 'cd', 'pq', 'xy']
nices = 0
count = 0
with open("data/5") as f:
    lines = f.readlines()
for line in lines:
    vowel = 0
    twice = False
    bad = False
    prev = None
    for c in line.strip():
        count += 1
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
print count
