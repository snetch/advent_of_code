from sys import stdin

# part 1
#card_types = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
# part 2
card_types = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

hand_types = ["high", "pair", "twopair", "three", "fullhouse", "four", "five"]

def less(card_a, card_b):
    return( card_types.index(card_a) < card_types.index(card_b) )

class Hand:
    def __init__(me, h, b):
        me.hand = h
        me.bid = b

        hand_totals = {}
        for c in h:
            # part 1: comment out the if J line
            # part 2: uncomment the if J line
            if c != "J":
                if c in hand_totals:
                    hand_totals[c] += 1
                else:
                    hand_totals[c] = 1
        hand_numbers = sorted( hand_totals.values() )

        if hand_numbers in [ [5], [4], [3], [2], [1], [] ]:
            me.type = "five"
        elif hand_numbers in [ [1,4], [1,3], [1,2], [1,1] ]:
            me.type = "four"
        elif hand_numbers in [ [2,3], [2,2] ]:
            me.type = "fullhouse"
        elif hand_numbers in [ [1,1,3], [1,1,2], [1,1,1] ]:
            me.type = "three"
        elif hand_numbers in [ [1,2,2] ]:
            me.type = "twopair"
        elif hand_numbers in [ [1,1,1,2], [1,1,1,1] ]:
            me.type = "pair"
        elif hand_numbers in [ [1,1,1,1,1] ]:
            me.type = "high"
        else:
            print("fuck!" + hand_numbers)
        
    def __lt__(me, other):
        if hand_types.index(me.type) < hand_types.index(other.type):
            return(True)
        if hand_types.index(me.type) > hand_types.index(other.type):
            return(False)
        for i in range(5):
            if me.hand[i] != other.hand[i]:
                return(less( me.hand[i], other.hand[i] ))

hands = []
for line in stdin:
    h, bid = line.split()
    hands.append( Hand(h, int(bid)) )

hands.sort()
bids_total = 0
for i in range( len(hands) ):
    print(hands[i].hand, hands[i].bid)
    bids_total += hands[i].bid * (i+1)

print(bids_total)
