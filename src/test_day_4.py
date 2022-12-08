import unittest

from day_4 import *

class Tests(unittest.TestCase):

   def test_is_section_contained_in_section(self):
      s1 = [2, 3, 4]
      s2 = [6, 7, 8]
      self.assertFalse(is_section_contained_in_section(s1, s2), "Section s1 should not be contained in section s2.")

      s1 = [2, 3, 4]
      s2 = [3]
      self.assertFalse(is_section_contained_in_section(s1, s2), "Section s1 not be contained in section s2.")

      s1 = [3]
      s2 = [2, 3, 4]
      self.assertTrue(is_section_contained_in_section(s1, s2), "Section s1 should be contained in section s2.")

      s1 = [3]
      s2 = [8, 9, 10]
      self.assertFalse(is_section_contained_in_section(s1, s2), "Section s1 should not be contained in section s2.")

      s1 = [3]
      s2 = [3, 4, 5]
      self.assertTrue(is_section_contained_in_section(s1, s2), "Section s1 should be contained in section s2.")

      s1 = [5]
      s2 = [3, 4, 5]
      self.assertTrue(is_section_contained_in_section(s1, s2), "Section s1 should be contained in section s2.")

      s1 = [3, 4, 5]
      s2 = [4, 5, 6]
      self.assertFalse(is_section_contained_in_section(s1, s2), "Section s1 should not be contained in section s2.")

      s1 = [5, 6, 7]
      s2 = [3, 4, 5]
      self.assertFalse(is_section_contained_in_section(s1, s2), "Section s1 should not be contained in section s2.")


   def test_expand_list(self):
      input = '2-5'
      result = [2, 3, 4, 5]
      self.assertEqual(expand_list(input), result, "Incorrect output returned.")

      input = '1-10'
      result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      self.assertEqual(expand_list(input), result, "Incorrect output returned.")

      input = '25'
      result = [25]
      self.assertEqual(expand_list(input), result, "Incorrect output returned.")

      input = '20-15'
      self.assertRaises(Exception, expand_list, input, msg="Input format incorrect.")



if __name__ == '__main__':
   unittest.main()
