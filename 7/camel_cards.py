from functools import total_ordering
import re

@total_ordering
class CamelCard:
    # T = 10
    FACE_ORDER = ['A', 'K', 'Q', 'J', 'T']

    def __init__(self, card_char) -> None:
        self.card_char = card_char
        assert self.is_valid_card(self.card_char), \
        f'{self.card_char} is not a valid camel card char'

    @classmethod
    def is_valid_card(cls, card_char) -> bool:
        return (card_char in cls.FACE_ORDER) or bool(re.match('^\d$', card_char))


    def is_face(self) -> bool:
        try:
            int(self.card_char)
            return False
        except:
            return True
        
    def __lt__(self, other):
        if  self.is_face():
            if other.is_face():
                #implement face card rank
                return (self.FACE_ORDER.index(self.card_char) - self.FACE_ORDER.index(other.card_char)) > 0 
            else:
                return False
        else:
            if other.is_face():
                return True
            else:
                return self.card_char < other.card_char
            
    def __eq__(self, other) -> bool:
        return self.card_char == other.card_char
    
    def __repr__(self) -> str:
        return self.card_char
    
    def __hash__(self) -> int:
        return hash(self.__repr__)

#@total_ordering
class CamelHand:

    HAND_ORDER = ['5k', '4k', 'fh', '3k', '2p', '1p', 'hc']
    def __init__(self, hand_str) -> None:
        self.hand_str = hand_str
        assert len(hand_str) == 5
        for card in self.hand_str:
            assert CamelCard.is_valid_card(card)

        card_set = set(self.hand_str)
        counts = []
        for card in card_set:
            counts.append(self.hand_str.count(card))
        #print(counts)

        if len(card_set) == 1:
            self.hand_type = '5k'
        elif len(card_set) == 2:
            if 4 in counts:
                self.hand_type ='4k'
            else:
                self.hand_type='fh'
        elif len(card_set) == 3:
            if 3 in counts:
                self.hand_type='3k'
            else:
                self.hand_type='2p'
        elif len(card_set) == 4:
            self.hand_type = '1p'
        else: #5 different cards
            self.hand_type = 'hc'
    

    def __lt__(self, other):
        if self.hand_type != other.hand_type:
            return (self.HAND_ORDER.index(self.hand_type) - self.HAND_ORDER.index(other.hand_type)) > 0
        else:
            for i, card_char in enumerate(self.hand_str):
                if CamelCard(card_char) != CamelCard(other.hand_str[i]):
                    return CamelCard(card_char) < CamelCard(other.hand_str[i])
        return False 

    def __repr__(self) -> str:
        return self.hand_str


def test_card_ordering(test_cards):            
    test_dict = {}
    for first_card in test_cards:
        this_card = CamelCard(first_card)
        this_test = []
        test_dict.update({first_card : this_test})
        for second_card in test_cards:
            other_card = CamelCard(second_card)
            this_test.append(f'{second_card}:{this_card < other_card}')
    return test_dict

f = open("input.txt", 'r')
line_list = [tuple(line.split()) for line in f.read().splitlines()]

print (line_list)

#card_test_dict = test_card_ordering(['A', 'T', '9', '3'])

#print(card_test_dict)

# CamelCard('JK')
# print(CamelCard.is_valid_card('9K'))

ranked_hands = []
bid_dict = {}
for line in line_list:
    hand_str = line[0]
    bid = int(line[1])
    ch = CamelHand(hand_str)
    #print(f'{hand_str}: {ch.hand_type}')
    ranked_hands.append(ch)
    bid_dict.update({ch : bid})

print(ranked_hands)
ranked_hands.sort()
print(ranked_hands)

#print(CamelHand('AAKKJ') < CamelHand('AAKK7'))

print(bid_dict)

win_list = [ (rank+1) * bid_dict[hand] for rank, hand in enumerate(ranked_hands)]
print(win_list)
print(sum(win_list))
#print(sum())
           

