from sys import stdin

preamble = 25
xmas = []

for line in stdin:
    xmas.append( int(line[:-1]) )

for i in range(preamble, len(xmas)):
    prev = xmas[ i-preamble : i ]
    valid = False
    for j in prev:
        if xmas[i] - j in prev and j != xmas[i] - j:
            valid = True
            break
    if not valid:
        print(xmas[i], "at position", i, "is invalid")
        inv = xmas[i]
        break

for i in range(len(xmas)):
    total = xmas[i]
    j = i+1
    while total < inv:
        total += xmas[j]
        j += 1
    if total == inv:
        print(xmas[i:j], sum(xmas[i:j]))
        break
