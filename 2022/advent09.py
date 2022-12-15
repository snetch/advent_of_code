from sys import stdin

def follow(headx, heady, tailx, taily):

    xdiff = headx - tailx
    ydiff = heady - taily

    if abs( xdiff ) <= 1 and abs( ydiff ) <= 1:
        return tailx, taily

    if headx == tailx:
        return tailx, taily + ydiff//abs(ydiff)

    if heady == taily:
        return tailx + xdiff//abs(xdiff), taily

    return tailx + xdiff//abs(xdiff), taily + ydiff//abs(ydiff)


visited1 = [(0,0)]
visited9 = [(0,0)]
ropex = [0,0,0,0,0,0,0,0,0,0]
ropey = [0,0,0,0,0,0,0,0,0,0]

for line in stdin:
    dir = line[0]
    num = int( line[2:] )

    for i in range(num):
        if dir == "R":
            ropex[0] += 1
        elif dir == "L":
            ropex[0] -= 1
        elif dir == "U":
            ropey[0] += 1
        elif dir == "D":
            ropey[0] -= 1

        for j in range(1, 10):
            ropex[j], ropey[j] = follow(ropex[j-1], ropey[j-1], ropex[j], ropey[j])

        visited1.append( (ropex[1], ropey[1]) )
        visited9.append( (ropex[9], ropey[9]) )

# print(visited1)
# print()

visited1.sort()
visited9.sort()
# print(visited1)
# print()

i = 1
while i<len(visited1):
    if visited1[i] == visited1[i-1]:
        visited1 = visited1[:i] + visited1[i+1:]
    else:
        i += 1

print(visited1)
print(i)

i = 1
while i<len(visited9):
    if visited9[i] == visited9[i-1]:
        visited9 = visited9[:i] + visited9[i+1:]
    else:
        i += 1

print(visited9)
print(i)
