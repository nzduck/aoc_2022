import unittest

from day_6 import *

class Tests(unittest.TestCase):

   def test_find_string_of_different_chars_in_buffer(self):
      pass


   
   def test_find_message_marker_in_buffer(self):
      param_list = [("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19)
         , ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23)
         , ("nppdvjthqldpwncqszvftbrmjlhg", 23)
         , ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29)
         , ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)]

      for p1, p2 in param_list:
            with self.subTest():
               result = find_message_marker_in_buffer(p1)
               self.assertEqual(result, p2, "Message marker was not found in correct position.")


   def test_find_packet_marker_in_buffer(self):
      param_list = [("bvwbjplbgvbhsrlpgdmjqwftvncz", 5)
         , ("nppdvjthqldpwncqszvftbrmjlhg", 6)
         , ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10)
         , ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)]

      for p1, p2 in param_list:
            with self.subTest():
               result = find_packet_marker_in_buffer(p1)
               self.assertEqual(result, p2, "Packet marker was not found in correct position.")


   def test_remove_front_of_list(self):
      l1 = ['1','2','3','4','5','6','7','8','9']
      to_remove_to = '3'
      expected_result = ['4','5','6','7','8','9']

      remove_front_of_list(l1, to_remove_to)

      self.assertEqual(l1, expected_result, "Lists are not the same.")

   
   def test_find_message_marker_in_buffer(self):
      pass


if __name__ == '__main__':
   unittest.main()
