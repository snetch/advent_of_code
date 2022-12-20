from sys import stdin

cubes = []
for line in stdin:
    cubes.append(  tuple(  [int(i) for i in line[:-1].split(",")]  )  )

n = len(cubes)


def adjacent(x, y):
    return(   abs(x[0]-y[0]) + abs(x[1]-y[1]) + abs(x[2]-y[2]) == 1   )
    

shared_sides = 0
for i in range( n ):
    for j in range( i+1, n ):
        if adjacent(cubes[i], cubes[j]):
            shared_sides += 1

print(n*6 - shared_sides*2)
