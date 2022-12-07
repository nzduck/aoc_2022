import unittest

from day_3 import *

class Tests(unittest.TestCase):
   
   def test_split_rucksack(self):
      self.assertEqual(split_rucksack('vJrwpWtwJgWrhcsFMMfFFhFp'), ('vJrwpWtwJgWr','hcsFMMfFFhFp'), "Rucksack not split properly.")
      self.assertEqual(split_rucksack('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'), ('jqHRNqRjqzjGDLGL','rsFMfFZSrLrFZsSL'), "Rucksack not split properly.")
      self.assertEqual(split_rucksack('PmmdzqPrVvPwwTWBwg'), ('PmmdzqPrV','vPwwTWBwg'), "Rucksack not split properly.")
      self.assertEqual(split_rucksack('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'), ('wMqvLMZHhHMvwLH','jbvcjnnSBnvTQFn'), "Rucksack not split properly.")
      self.assertEqual(split_rucksack('ttgJtRGJQctTZtZT'), ('ttgJtRGJ','QctTZtZT'), "Rucksack not split properly.")
      self.assertEqual(split_rucksack('CrZsJsPPZsGzwwsLwLmpwMDw'), ('CrZsJsPPZsGz','wwsLwLmpwMDw'), "Rucksack not split properly.")

   def test_find_common(self):
      self.assertEqual(find_common('vJrwpWtwJgWr','hcsFMMfFFhFp'), 'p', "Common element was not found.")
      self.assertEqual(find_common('jqHRNqRjqzjGDLGL','rsFMfFZSrLrFZsSL'), 'L', "Common element was not found.")
      self.assertEqual(find_common('PmmdzqPrV','vPwwTWBwg'), 'P', "Common element was not found.")
      self.assertEqual(find_common('wMqvLMZHhHMvwLH','jbvcjnnSBnvTQFn'), 'v', "Common element was not found.")
      self.assertEqual(find_common('ttgJtRGJ','QctTZtZT'), 't', "Common element was not found.")
      self.assertEqual(find_common('CrZsJsPPZsGz','wwsLwLmpwMDw'), 's', "Common element was not found.")

   def test_map_to_priority(self):
      self.assertEqual(map_to_priority('a'), 1, "Mapped to incorrect priority.")
      self.assertEqual(map_to_priority('b'), 2, "Mapped to incorrect priority.")
      self.assertEqual(map_to_priority('y'), 25, "Mapped to incorrect priority.")
      self.assertEqual(map_to_priority('z'), 26, "Mapped to incorrect priority.")
      self.assertEqual(map_to_priority('A'), 27, "Mapped to incorrect priority.")
      self.assertEqual(map_to_priority('B'), 28, "Mapped to incorrect priority.")
      self.assertEqual(map_to_priority('Y'), 51, "Mapped to incorrect priority.")
      self.assertEqual(map_to_priority('Z'), 52, "Mapped to incorrect priority.")

   def test_find_common_element_in_group(self):
      self.assertEqual(find_common_element_in_group(
         'vJrwpWtwJgWrhcsFMMfFFhFp'
         , 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
         , 'PmmdzqPrVvPwwTWBwg'), 'r', "Incorrect common element found in group.")
      self.assertEqual(find_common_element_in_group(
         'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'
         , 'ttgJtRGJQctTZtZT'
         , 'CrZsJsPPZsGzwwsLwLmpwMDw'), 'Z', "Incorrect common element found in group.")


if __name__ == '__main__':
   unittest.main()

