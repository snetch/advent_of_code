# find the corresponding closed bracket position
def closing(line, opening):
    level = 1
    location = opening
    while level > 0:
        next_opening = line.find("[", location+1)
        next_closing = line.find("]", location+1)
        if next_opening > -1 and next_opening < next_closing:
            level += 1
            location = next_opening
        else:
            level -= 1
            location = next_closing
    return(location)


# generate a list of ints and lists that corresponds to the string
def generate(line):
    list = []
    i = 1
    while i < len(line)-1:
        if line[i] == "[":
            end = closing(line, i)
            list.append( generate(line[i:end+1]) )
        else:
            end = line.find(",", i)
            if end == -1:
                end = line.find("]", i)
            end -= 1
            list.append( int(line[i:end+1]) )
        i = end+2
    return( list )


# return
# -1 if list1 < list2,
# 0 if equal,
# 1 if list1 > list2
def ordered(list1, list2):
    shortest_length = len(list1) if len(list1) < len(list2) else len(list2)

    for i in range(shortest_length):
        x = list1[i]
        y = list2[i]
        if type(x) == int and type(y) == int:
            if x<y:
                return(-1)
            if x>y:
                return(1)
        else:
            if type(x) == list and type(y) == int:
                y = [y]
            elif type(x) == int and type(y) == list:
                x = [x]
            #elif type(x) == list and type(y) == list:

            element = ordered(x, y)
            if element == -1:
                return(-1)
            if element == 1:
                return(1)

    if len(list1) < len(list2):
        return(-1)
    elif len(list1) > len(list2):
        return(1)
    else:
        return(0)



index = 0
sum = 0
all_packets = [   [[2]], [[6]]   ]
index_total = 2

while True:
    index += 1
    left = generate( input() )
    right = generate( input() )

    if ordered(left, right) == -1:
        sum += index

    all_packets.append( left )
    index_total += 1

    i = index_total-1
    while ordered( all_packets[i-1], all_packets[i] ) > -1 and i > 0:
        spare = all_packets[i]
        all_packets[i] = all_packets[i-1]
        all_packets[i-1] = spare
        i -= 1

    all_packets.append( right )
    index_total += 1

    i = index_total-1
    while ordered( all_packets[i-1], all_packets[i] ) > -1 and i > 0:
        spare = all_packets[i]
        all_packets[i] = all_packets[i-1]
        all_packets[i-1] = spare
        i -= 1

    try:
        line = input()
    except EOFError:
        break

print(sum)

for i in range( len(all_packets) ):
    if all_packets[i] == [[2]]:
        print(i+1)
        index1 = i+1
    if all_packets[i] == [[6]]:
        print(i+1)
        index2 = i+1

print(index1 * index2)
