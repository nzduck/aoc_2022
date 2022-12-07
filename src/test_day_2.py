import unittest

from day_2 import *

class Tests(unittest.TestCase):

   def test_map_code_to_object(self):
      self.assertEqual(map_code_to_object("A"), OBJECT_ROCK, "Should be rock.")
      self.assertEqual(map_code_to_object("B"), OBJECT_PAPER, "Should be paper.")
      self.assertEqual(map_code_to_object("C"), OBJECT_SCISSORS, "Should be scissors.")

   def test_map_code_to_outcome(self):
      self.assertEqual(map_code_to_outcome("X"), OUTCOME_LOSS, "Should be a loss.")
      self.assertEqual(map_code_to_outcome("Y"), OUTCOME_DRAW, "Should be a draw.")
      self.assertEqual(map_code_to_outcome("Z"), OUTCOME_WIN, "Should be a win.")

   def test_score_outcome(self):
      self.assertEqual(score_outcome(OUTCOME_WIN), 6, "Should be 6.")
      self.assertEqual(score_outcome(OUTCOME_LOSS), 0, "Should be 0.")
      self.assertEqual(score_outcome(OUTCOME_DRAW), 3, "Should be 3.")

   def test_score_object_used(self):
      self.assertEqual(score_object_used(OBJECT_ROCK), 1, "Should be 1.")
      self.assertEqual(score_object_used(OBJECT_PAPER), 2, "Should be 2.")
      self.assertEqual(score_object_used(OBJECT_SCISSORS), 3, "Should be 3.")

   def test_find_hand_to_play(self):
      self.assertEqual(find_hand_to_play(OBJECT_ROCK, OUTCOME_WIN), OBJECT_PAPER, "Should be paper 1.")
      self.assertEqual(find_hand_to_play(OBJECT_ROCK, OUTCOME_DRAW), OBJECT_ROCK, "Should be rock 1.")
      self.assertEqual(find_hand_to_play(OBJECT_ROCK, OUTCOME_LOSS), OBJECT_SCISSORS, "Should be scissors 1.")

      self.assertEqual(find_hand_to_play(OBJECT_PAPER, OUTCOME_WIN), OBJECT_SCISSORS, "Should be scissors 2.")
      self.assertEqual(find_hand_to_play(OBJECT_PAPER, OUTCOME_DRAW), OBJECT_PAPER, "Should be paper 2.")
      self.assertEqual(find_hand_to_play(OBJECT_PAPER, OUTCOME_LOSS), OBJECT_ROCK, "Should be rock 2.")

      self.assertEqual(find_hand_to_play(OBJECT_SCISSORS, OUTCOME_WIN), OBJECT_ROCK, "Should be rock 3.")
      self.assertEqual(find_hand_to_play(OBJECT_SCISSORS, OUTCOME_DRAW), OBJECT_SCISSORS, "Should be scissors 3.")
      self.assertEqual(find_hand_to_play(OBJECT_SCISSORS, OUTCOME_LOSS), OBJECT_PAPER, "Should be paper 3.")

if __name__ == '__main__':
   unittest.main()