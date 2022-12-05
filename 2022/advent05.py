method = "part 2"  # set to "part 1" or "part 2" accordingly

line = input()
n = len(line) // 4 + 1  # thankfully the input is padded with spaces immediately
stacks = []
for i in range(n):
    stacks.append([])

while line:
    for i in range(n):
        if line[i*4+1] != " ":
            stacks[i].insert(0, line[i*4+1])
    line = input()

for s in stacks:
    print(s)
print()

from sys import stdin
for line in stdin:  # just the leftover stdin. Mix of input styles, I know, sorry
    amount, source, dest = [int(x) for x in line[:-1].split(" ") if x[0] in "0123456789"]  # python magic

    if method == "part 1":
        for i in range(amount):
            c = stacks[source-1].pop()
            stacks[dest-1].append(c)
    else:
        cranestack = []
        for i in range(amount):
            c = stacks[source-1].pop()
            cranestack.insert(0, c)
        stacks[dest-1] += cranestack

tops = ""
for s in stacks:
    print(s)
    tops += s[-1]

print(tops)
