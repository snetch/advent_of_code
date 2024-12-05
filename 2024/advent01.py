from sys import stdin

alist = []
blist = []

for line in stdin:
    a, b = line.split("   ")
    alist.append(int(a))
    blist.append(int(b))

# part 1

alist.sort()
blist.sort()

diffsum = 0

for i in range(len(alist)):
    diffsum += abs( alist[i]-blist[i] )

print(diffsum)

# part 2

simscore = 0

for i in alist:
    for j in blist:
        if i == j:
            simscore += i

print(simscore)
