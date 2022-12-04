from sys import stdin

score1 = 0
score2 = 0

for line in stdin:

    diff = ord(line[2]) - ord(line[0]) - 22
    diffscore = diff%3*3
    throwscore = ord(line[2]) - 87
    score1 += diffscore + throwscore

    opponent_figure = ord(line[0]) - 64  # rock=1
    win_or_lose = ord(line[2]) - 89  # centered on draw=0
    my_figure = (opponent_figure + win_or_lose - 1) % 3 + 1
    score2 += my_figure + win_or_lose*3 + 3

print (score1, score2)
