VALUE_OF_ROCK = 1
VALUE_OF_PAPER = 2
VALUE_OF_SCISSORS = 3

VALUE_OF_LOSS = 0
VALUE_OF_DRAW = 3
VALUE_OF_WIN = 6

OBJECT_ROCK = 0
OBJECT_PAPER = 1
OBJECT_SCISSORS = 2

OUTCOME_LOSS = 0
OUTCOME_DRAW = 1
OUTCOME_WIN = 2

OBJECTS = ["rock", "paper", "scissors"]
OUTCOMES = ["loss", "draw", "win"]

def map_code_to_object(code):

   ROCK_CODE_THEM = "A"
   PAPER_CODE_THEM = "B"
   SCISSORS_CODE_THEM = "C"

   if code == ROCK_CODE_THEM:
      return OBJECT_ROCK

   if code == PAPER_CODE_THEM:
      return OBJECT_PAPER

   if code == SCISSORS_CODE_THEM:
      return OBJECT_SCISSORS

   raise Exception("Object not found for map code.")


def map_code_to_outcome(code):

   CODE_LOSE = "X"
   CODE_DRAW = "Y"
   CODE_WIN = "Z"

   if code == CODE_LOSE:
      return OUTCOME_LOSS

   if code == CODE_DRAW:
      return OUTCOME_DRAW

   if code == CODE_WIN:
      return OUTCOME_WIN

   raise Exception("Outcome not found for map code.")


def score_outcome(outcome):
   if outcome == OUTCOME_WIN:
      return VALUE_OF_WIN

   if outcome == OUTCOME_DRAW:
      return VALUE_OF_DRAW

   if outcome == OUTCOME_LOSS:
      return VALUE_OF_LOSS

   raise Exception("Unknown outcome encountered.")


def score_object_used(object):
   if object == OBJECT_ROCK:
      return VALUE_OF_ROCK

   if object == OBJECT_PAPER:
      return VALUE_OF_PAPER

   if object == OBJECT_SCISSORS:
      return VALUE_OF_SCISSORS

   raise Exception("Unknown object value encountered.")


def find_hand_to_play(their_hand, desired_outcome):
   if desired_outcome == OUTCOME_DRAW:
      return their_hand

   if desired_outcome == OUTCOME_WIN:
      if their_hand == OBJECT_ROCK:
         return OBJECT_PAPER
      elif their_hand == OBJECT_PAPER:
         return OBJECT_SCISSORS
      else:
         return OBJECT_ROCK

   elif desired_outcome == OUTCOME_LOSS:
      if their_hand == OBJECT_ROCK:
         return OBJECT_SCISSORS
      elif their_hand == OBJECT_PAPER:
         return OBJECT_ROCK
      else:
         return OBJECT_PAPER


def main():
   # open the data file
   with open('.\data\data.txt', 'r') as f:
      all_data = f.readlines()

   our_total_score = 0
   count = 0

   for l in all_data:
      vals = l.strip().split()

      count += 1

      their_hand = map_code_to_object(vals[0])
      outcome_of_hand = map_code_to_outcome(vals[1])

      score_for_outcome = score_outcome(outcome_of_hand)

      our_hand = find_hand_to_play(their_hand, outcome_of_hand)
      score_for_object = score_object_used(our_hand)

      print(f"Playing {OBJECTS[their_hand].upper()} (them) and wanting a {OUTCOMES[outcome_of_hand].upper()} - we want {OBJECTS[our_hand].upper()} (us).")
      print(f"Score for the outcome: {score_for_outcome} and score for the object {score_for_object} - a total of {score_for_outcome + score_for_object}.")
      print()

      our_score = score_for_outcome + score_for_object
      our_total_score += our_score

   print(f"{count} hands played. Final score for us was: {our_total_score}!")


if __name__ == '__main__':
   main()

