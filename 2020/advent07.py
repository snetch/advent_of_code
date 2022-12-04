from sys import stdin

bags = {}

for line in stdin:
    # A B bags contain X C D bags, Y E F bags, Z G H bags.
    # XYZ are numbers, ABCDEFGH are words.
    line = line[:-1].split(" ")
    outer = line[0] + " " + line[1]
    
    contents = {}
    counter = 4 # after "contain"
    if line[counter] != "no":
        while True:
            inner = line[counter+1] + " " + line[counter+2]
            contents[inner] = line[counter]
            if line[counter+3][-1] == ".":
                break
            counter += 4
    bags[outer] = contents

search = ["shiny gold"]
while True:
    # list(set(x)) removes duplicates from x
    # b in bags is the type of outer bags
    # bags[b] is the sub-dictionary of b's contents
    search_iteration = list(set( [b for b in bags for contents in bags[b] if contents in search and b not in search] ))
    search += search_iteration
    if search_iteration == []:
        break
print(len(search)-1)

def total(outer):
    if len(bags[outer]) == 0:
        return(1)
    t = 1
    for inner in bags[outer]:
        t += total(inner) * int(bags[outer][inner])
    return(t)

print(total("shiny gold")-1)



