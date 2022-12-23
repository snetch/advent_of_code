from sys import stdin

PART = 2
decryption_key = 811589153

numbers = []
indexes = []
count = 0

for line in stdin:
    numbers.append( int(line[:-1]) )
    indexes.append( count )
    count += 1

if PART == 2:
    for i in range(count):
        numbers[i] *= decryption_key
#print(numbers)
#print(indexes)

def mix(numbers, indexes, count):
    
    for i in range(count):
        old_index = indexes.index(i)
        new_index = ( old_index + numbers[old_index] )  %  (count-1)
    #    print("moving from", old_index, "to", new_index)
        current = numbers.pop(old_index)
        current_index = indexes.pop(old_index)
        numbers.insert(new_index, current)
        indexes.insert(new_index, current_index)

    #    print(numbers)

if PART == 1:
    number_of_mixes = 1
elif PART == 2:
    number_of_mixes = 10
else:
    print("wtf")

for i in range(number_of_mixes):
    mix(numbers, indexes, count)
#    print(numbers)
#    print(indexes)

zero = numbers.index(0)
coordinates = [
    numbers[(zero+1000)%count],
    numbers[(zero+2000)%count],
    numbers[(zero+3000)%count]
]
print(coordinates, sum(coordinates))

