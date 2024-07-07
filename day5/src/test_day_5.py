import unittest

from day_5 import *

class Tests(unittest.TestCase):

   def test_move_elem(self):
      l1 = [1,2,3,4]
      l2 = [6,7,8,9]
      expected_l1 = [1,2]
      expected_l2 = [6,7,8,9,4,3]
      
      move_elem(l1, l2, 2)

      self.assertEqual(l1, expected_l1, "From lists are not equal.")
      self.assertEqual(l2, expected_l2, "Destination lists are not equal.")


   def test_split_command(self):
      num = 0
      from_list = ""
      to_list = ""
      c1 = "move 2 from 7 to 3"

      t = split_command(c1)

      self.assertEqual(t[0], 2, "Number to move is incorrect.")
      self.assertEqual(t[1], "7", "Number to move is incorrect.")
      self.assertEqual(t[2], "3", "Number to move is incorrect.")


   def test_generate_code(self):
      d = {
         "1" : [1,2,3],
         "2" : [4,5,6,7],
         "3" : [8,9,0]
      }
      expected = "370"

      self.assertEqual(generate_code(d), expected, "Generated code does not equal expected code.")


   def test_move_elem_multiple(self):
      l1 = [1,2,3,4]
      l2 = [6,7,8,9]
      expected_l1 = [1,2]
      expected_l2 = [6,7,8,9,3,4]

      move_elem_multiple(l1, l2, 2)

      self.assertEqual(l1, expected_l1, "From lists are not equal.")
      self.assertEqual(l2, expected_l2, "Destination lists are not equal.")


if __name__ == '__main__':
   unittest.main()
