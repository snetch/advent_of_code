from sys import stdin

max_id = 0
id_list = []
for line in stdin:
    row = 0
    for i in line[:7]: # turn line[:7] binary into decimal. F=0, B=1
        row *= 2
        row += (i=="B")

    seat = 0
    for i in line[7:10]: # turn line[7:10] binary into decimal. L=0, R=1
        seat *= 2
        seat += (i=="R")

    seat_id = row*8 + seat
    id_list.append(seat_id)
    if seat_id > max_id:
        max_id = seat_id
#    print(line, row, seat, row*8 + seat)
print(max_id)

id_list.sort()
for i in range(1, len(id_list)):
    if id_list[i] - id_list[i-1] > 1:
        print(id_list[i])