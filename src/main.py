VALUE_OF_ROCK = 1
VALUE_OF_PAPER = 2
VALUE_OF_SCISSORS = 3

VALUE_OF_LOSS = 0
VALUE_OF_DRAW = 3
VALUE_OF_WIN = 6

OBJECT_ROCK = 0
OBJECT_PAPER = 1
OBJECT_SCISSORS = 2

OBJECTS = ["rock", "paper", "scissors"]

def map_code_to_object(code):

   ROCK_CODE_THEM = "A"
   PAPER_CODE_THEM = "B"
   SCISSORS_CODE_THEM = "C"

   ROCK_CODE_US = "X"
   PAPER_CODE_US = "Y"
   SCISSORS_CODE_US = "Z"

   if code == ROCK_CODE_THEM or code == ROCK_CODE_US:
      return OBJECT_ROCK

   if code == PAPER_CODE_THEM or code == PAPER_CODE_US:
      return OBJECT_PAPER

   if code == SCISSORS_CODE_THEM or code == SCISSORS_CODE_US:
      return OBJECT_SCISSORS

   raise Exception("Object not found for map code.")


def score_outcome(hand_to_test_against, hand_to_test):
   if hand_to_test_against == hand_to_test:
      print(" Both hands were the same - draw!. (3 points)")
      return VALUE_OF_DRAW

   print(f" First hand was {OBJECTS[hand_to_test_against].upper()} and second hand was {OBJECTS[hand_to_test].upper()}.")

   if hand_to_test_against == OBJECT_ROCK and hand_to_test == OBJECT_PAPER:
      print("  Second hand wins! (6 points)")
      return VALUE_OF_WIN

   if hand_to_test_against == OBJECT_SCISSORS and hand_to_test == OBJECT_ROCK:
      print("  Second hand wins! (6 points)")
      return VALUE_OF_WIN

   if hand_to_test_against == OBJECT_PAPER and hand_to_test == OBJECT_SCISSORS:
      print("  Second hand wins! (6 points)")
      return VALUE_OF_WIN

   print("  First hand wins! (0 points)")
   return VALUE_OF_LOSS


def score_object_used(object):
   if object == OBJECT_ROCK:
      return VALUE_OF_ROCK

   if object == OBJECT_PAPER:
      return VALUE_OF_PAPER

   if object == OBJECT_SCISSORS:
      return VALUE_OF_SCISSORS

   raise Exception("Unknown object value encountered.")


# open the data file
with open('.\data\data.txt', 'r') as f:
   all_data = f.readlines()

our_total_score = 0

for l in all_data:
   vals = l.strip().split()

   their_hand = map_code_to_object(vals[0])
   our_hand = map_code_to_object(vals[1])

   print(f"Playing {OBJECTS[their_hand].upper()} (them) against {OBJECTS[our_hand].upper()} (us).")

   score_for_outcome = score_outcome(their_hand, our_hand)
   score_for_object = score_object_used(our_hand)

   print(f"Score for the outcome: {score_for_outcome} and score for the object {score_for_object} - a total of {score_for_outcome + score_for_object}.")

   our_score = score_for_outcome + score_for_object
   our_total_score += our_score

print(f"Final score for us was: {our_total_score}!")
