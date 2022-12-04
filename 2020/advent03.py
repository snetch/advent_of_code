from sys import stdin

location1, trees1 = 0, 0
location2, trees2 = 0, 0
location3, trees3 = 0, 0
location4, trees4 = 0, 0
location5, trees5, skip5 = 0, 0, 0

for line in stdin:
    line = line[:-1] # newline is for some reason included

    if line[ location1 % len(line) ] == '#':
        trees1 += 1
    location1 += 1

    if line[ location2 % len(line) ] == '#':
        trees2 += 1
    location2 += 3

    if line[ location3 % len(line) ] == '#':
        trees3 += 1
    location3 += 5

    if line[ location4 % len(line) ] == '#':
        trees4 += 1
    location4 += 7

    if skip5 == 0:
        if line[ location5 % len(line) ] == '#':
            trees5 += 1
        location5 += 1
        skip5 = 1
    else:
        skip5 = 0

print(trees1, trees2, trees3, trees4, trees5, trees1*trees2*trees3*trees4*trees5)
