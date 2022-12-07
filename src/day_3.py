def split_rucksack(contents):
   a = len(contents) // 2
   return (contents[:a], contents[a:])

def find_common(elem_1, elem_2):
   for e in elem_1:
      if e in elem_2:
         return e

def map_to_priority(val):
   codes = ['a','b','c','d','e','f','g','h','i','j'
      ,'k','l','m','n','o','p','q','r','s','t','u'
      ,'v','w','x','y','z','A','B','C','D','E','F'
      ,'G','H','I','J','K','L','M','N','O','P','Q'
      ,'R','S','T','U','V','W','X','Y','Z']
   return codes.index(val) + 1

def find_common_element_in_group(ruck_1, ruck_2, ruck_3):
   for e1 in ruck_1:
      if e1 in ruck_2:
         if e1 in ruck_3:
            return e1


def day_1_answer(all_data):
   sum_priorities = 0
   count = 0

   for contents in all_data:
      count += 1
      compart_1, compart_2 = split_rucksack(contents)
      val = find_common(compart_1, compart_2)
      sum_priorities += map_to_priority(val)

   print(f"{count} records processed. Sum of priorities is {sum_priorities}.")

def day_2_answer(all_data):
   sum_priorities = 0
   count = 0

   for i in range(0, len(all_data), 3):
      count += 1

      ruck_1 = all_data[i]
      ruck_2 = all_data[i + 1]
      ruck_3 = all_data[i + 2]

      val = find_common_element_in_group(ruck_1, ruck_2, ruck_3)
      sum_priorities += map_to_priority(val)

   print(f"{count} groups processed. Sum of priorities is {sum_priorities}.")



def main():
      # open the data file
   with open('.\data\data.txt', 'r') as f:
      all_data = f.readlines()

   day_1_answer(all_data)

   day_2_answer(all_data)

if __name__ == '__main__':
   main()
