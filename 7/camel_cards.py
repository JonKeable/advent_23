from functools import total_ordering

f = open("test.txt", 'r')
line_list = [tuple(line.split()) for line in f.read().splitlines()]

print (line_list)

class CamelCard:
    # T = 10
    FACE_ORDER = ['A', 'K', 'Q', 'J', 'T']

    def __init__(self, card_char) -> None:
        self.card_char = card_char

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
            
test_cards = ['A', 'T', '9', '3']
test_dict = {}
for first_card in test_cards:
    this_card = CamelCard(first_card)
    this_test = []
    test_dict.update({first_card : this_test})
    for second_card in test_cards:
        other_card = CamelCard(second_card)
        this_test.append(this_card < other_card)
        
print(test_dict)
            
           

