PART = 2

monkeys = []
operations = []
tests = []
truethrow = []
falsethrow = []
inspect_count = []

# ADD an empty line at the START of the input for the try to work properly

while True:
    try:
        line = input()
    except EOFError:
        print("EOF")
        break

    input()  # Monkey #
    monkeys.append(      [ int(i) for i in input()[18:].split(", ") ]   )
    operations.append(   input()[23:]                                   )  # includes just the operation and the second operand
    tests.append(        int( input()[21:] )                            )
    truethrow.append(    int( input()[29] )                             )
    falsethrow.append(   int( input()[30] )                             )
    inspect_count.append(0)

print(monkeys, operations, tests, truethrow, falsethrow)

# I checked, they are all primes, so the LCM will just be their product
LCM = 1
for i in tests:
    LCM *= i
print(LCM)
print()

if PART == 1:
    rounds = 20
elif PART == 2:
    rounds = 10000

for i in range(rounds):
    for j in range( len(monkeys) ):
        while len( monkeys[j] ) > 0:

            inspect_count[j] += 1
            current = monkeys[j].pop(0)

            op = operations[j][0]
            if operations[j][2:] == "old":
                operand = current
            else:
                operand = int( operations[j][2:] )

            if op == "+":
                next = current + operand
            elif op == "*":
                next = current * operand

            if PART == 1:
                next //= 3
            elif PART == 2:
                next %= LCM

            if next % tests[j] == 0:
                monkeys[ truethrow[j] ].append(next)
            else:
                monkeys[ falsethrow[j] ].append(next)

    if i == 0 or i == 19 or i % 1000 == 999:
        print(monkeys)
        print(inspect_count)

inspect_count.sort(reverse = True)
print(inspect_count)
print(inspect_count[0] * inspect_count[1])
