from sys import stdin

adapters = [0]
for line in stdin:
    adapters.append( int(line[:-1]) )
adapters.sort()
adapters.append( adapters[-1] + 3 )

ones = 0
threes = 0
max = adapters[-1]
for i in range( 1, len(adapters) ):
    if adapters[i] - adapters[i-1] == 1:
        ones += 1
    if adapters[i] - adapters[i-1] == 3:
        threes += 1

print(adapters)
print(ones, threes, ones*threes)

ways = [1] + [0]*max
adapters = adapters[1:] # remove the 0
prev = 0
if 1 in adapters:
    ways[1] = ways[0]
    adapters = adapters[1:]
    prev = 1
if 2 in adapters:
    ways[2] = ways[0] + ways[1]
    adapters = adapters[1:]
    prev = 2
for joltage in adapters:
    ways[joltage] = ways[joltage-3] + ways[joltage-2] + ways[joltage-1]
    prev = joltage

print(ways)
print(ways[-1])