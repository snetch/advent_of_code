import re


# greatest common denominator
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return(x)


# least common multiple
def lcm(x, y):
    return( (x*y) // gcd(x,y) )


instructions = input()
input()

next = {}
a_ends = []
while True:
    try:
        node, left, right, extra = re.split( ' = \(|, |\)', input() )
        if node[2] == "A":
            a_ends.append(node+"0")
        for i in range( len(instructions) ):
            if instructions[i] == "L":
                next[ node + str(i) ] = left + str( (i+1)%len(instructions) )
            else:
                next[ node + str(i) ] = right + str( (i+1)%len(instructions) )
    except EOFError:
        print("EOF")
        break

#for i in next:
#    print(i, next[i])
#print()

# PART 1 
#current = "AAA0"
#for i in range(1, 1000000):
#    current = next[current]
#    if current[:3] == "ZZZ":
#        print(current, i)
#        break

least_multiple = 1
for attempt in a_ends:
    current = attempt
#    found = 0
#    found_i = 0
    for i in range(1, 1000000):
        current = next[current]
        if current[2] == "Z":
            least_multiple = lcm( least_multiple, i )
            print(current, i, least_multiple)  #, i-found_i)
#            found += 1
#            found_i = i
            least_multiple = lcm( least_multiple, i )
#            if found > 5:
            break

