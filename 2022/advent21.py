from sys import stdin

class Monkey:
    def __init__(self, name, job):
        self.name = name
        job_parts = job.split(" ")
        if len(job_parts) == 1:
            self.calculation = False
            self.value = int(job)
        else:
            self.calculation = True
            self.value = None
            self.ref1, self.op, self.ref2 = job.split(" ")


monkeys = []
monkey_index = {}
count = 0

for line in stdin:
    line = line[:-1].split(": ")
    m = Monkey(line[0], line[1] )
    monkeys.append(m)
    monkey_index[m.name] = count
    count += 1

root_index = monkey_index["root"]
humn_index = monkey_index["humn"]


# this method assumes no calculations have been done yet and monkeys that need calculations don't have a value yet
# and then sets those values
def get_value(m):
    global monkeys, monkey_index

    if not m.calculation:
        return(m.value)

    ref1 = get_value( monkeys[ monkey_index[m.ref1] ] )
    ref2 = get_value( monkeys[ monkey_index[m.ref2] ] )

    if m.op == "+":
        m.value = ref1 + ref2
    elif m.op == "-":
        m.value = ref1 - ref2
    elif m.op == "*":
        m.value = ref1 * ref2
    elif m.op == "/":
        m.value = ref1 / ref2
#    elif m.op == "=":
#        return(ref1 == ref2)
    else:
        print("wtf2")
    return(m.value)


print(get_value(monkeys[root_index]))

monkeys[root_index].op = "="


# this one assumes that the calculations already ran, and reads all the saved results
# return[0] is whether "humn" is somewhere in the tree
# if no humn in the tree: return[1] is the calculated value
# if yes humn in the tree: return[1] and [2] are the multiplyer and the addition for a "humn" formula
def reverse_search(m):
    global monkeys, monkey_index

    if m.name == "humn":
        return( [True, 1, 0] )
    if not m.calculation:
        return( [False, m.value ] )

    left = reverse_search(monkeys[monkey_index[m.ref1]])
    right = reverse_search(monkeys[monkey_index[m.ref2]])
    
#    if m.name in ["sjmn", "drzm", "dbpl", "hmdt", "zczc"]:
#        print(m.name, left, m.op, right)

    if not left[0] and not right[0]:
        return( [False, m.value] )

    # humn is on the left side, extra operand is right[1]
    if left[0]:
        if m.op == "+":
            return([  True, left[1], left[2] + right[1]  ])
        elif m.op == "-":
            return([  True, left[1], left[2] - right[1]  ])
        elif m.op == "*":
            return([  True, left[1]*right[1], left[2]*right[1]  ])
        elif m.op == "/":
            return([  True, left[1]/right[1], left[2]/right[1]  ])
        elif m.op == "=":
            print(left[1], "* humn +", left[2], "=", right[1])
            print("humn =", (right[1]-left[2])/left[1])
        else:
            print("wtf3")

    # humn is on the right side, extra operand is left[1]
    else:
        if m.op == "+":
            return([  True, right[1], right[2]+left[1]  ])
        elif m.op == "-":
            return([  True, right[1]*-1, left[1]-right[2]  ])
        elif m.op == "*":
            return([  True, right[1]*left[1], right[2]*left[1]  ])
        elif m.op == "/":
            print("fuck") #return([  True,   ])
        elif m.op == "=":
            print(left[1], "=", right[1], "* humn +", right[2])
            print("humn =", (left[1]-right[2])/right[1])
        else:
            print("wtf4")

reverse_search(monkeys[root_index])

# read the equation that was just printed, solve, get the answer, plug right into this next for loop range to verify
#for guess in range(301, 302):
#for guess in range(3305669217840, 3305669217841):
#    if guess % 5000 == 0:
#    print("trying", guess)

    # init
#    for i in monkeys:
#        if i.calculation:
#            i.value = None

    # actual run
#    monkeys[humn_index].value = guess
#    if get_value(monkeys[root_index]):
#        print("found value", guess, "for humn makes root equal")
