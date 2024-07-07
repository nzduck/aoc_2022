def is_section_contained_in_section(s1, s2):
   for e in s1:
      if e not in s2:
         return False

   return True


def expand_list(to_expand):

   if '-' not in to_expand:
      lower = upper = int(to_expand)
   else:
      lower, upper = to_expand.strip().split('-')

      if int(lower) > int(upper):
         print(lower,upper)
         raise Exception("Lower bound of index cannot be greater than upper bound.")

   return list(range(int(lower), int(upper) + 1))


def day_4_part_1_answer(input):

   rows_processed = 0
   count = 0

   for l in input:
      rows_processed += 1
      first, second = l.strip().split(',')

      ex_1 = expand_list(first)
      ex_2 = expand_list(second)
      if is_section_contained_in_section(ex_1, ex_2) or \
         is_section_contained_in_section(ex_2, ex_1):
         count += 1

   print(f"{rows_processed} rows processed. {count} fully overlapping sections found.")


def day_4_part_2_answer(input):

   rows_processed = 0
   count = 0

   for l in input:
      rows_processed += 1
      first, second = l.strip().split(',')

      ex_1 = expand_list(first)
      ex_2 = expand_list(second)

      if lists_intersect(ex_1, ex_2):
         count += 1

   print(f"{rows_processed} rows processed. {count} intersecting sections found.")


def lists_intersect(l1, l2):
   result =  [value for value in l1 if value in l2]
   return result != []


def main():
   
   # open the data file
   with open('.\data\data.txt', 'r') as f:
      all_data = f.readlines()

   day_4_part_1_answer(all_data)
   day_4_part_2_answer(all_data)
   


if __name__ == '__main__':
   main()
