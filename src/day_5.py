def init_map():
   map = {
      '1': ['H','T','Z','D'],
      '2': ['Q','R','W','T','G','C','S'],
      '3': ['P','B','F','Q','N','R','C','H'],
      '4': ['L','C','N','F','H','Z'],
      '5': ['G','L','F','Q','S'],
      '6': ['V','P','W','Z','B','R','C','S'],
      '7': ['Z','F','J'],
      '8': ['D','L','V','Z','R','H','Q'],
      '9': ['B','H','G','N','F','Z','L','D']    
   }

   return map

def move_elem(l1, l2, num):
   for n in range(num):
      l2.append(l1.pop())


def split_command(c):
   c1 = c.split(' ')
   num = int(c1[1])
   from_list = c1[3]
   to_list = c1[5]

   return tuple((num, from_list, to_list))


def generate_code(map):
   ret = ""
   for k in map.keys():
      v = map.get(k).pop()
      ret += str(v)

   return ret


def day_5_part_1_answer(all_data):

   map = init_map()

   count = 0
   for l in all_data:
      if l.startswith('move '):
         count += 1

         print(l)
         t = split_command(l.strip()) 

         print(map.get(t[1]), map.get(t[2]))
         move_elem(map.get(t[1]), map.get(t[2]), t[0])
         print(map.get(t[1]), map.get(t[2]))

         print()

   print(f"{count} records processed. Code is {generate_code(map)}")


def day_5_part_2_answer(all_data):
   pass


def main():
   
   # open the data file
   with open('.\data\data.txt', 'r') as f:
      all_data = f.readlines()

   day_5_part_1_answer(all_data)
   day_5_part_2_answer(all_data)
   


if __name__ == '__main__':
   main()
