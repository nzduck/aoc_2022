def find_string_of_different_chars_in_buffer(buff, num):
   count = 0
   seen = []

   for c in buff:
      count += 1

      if c in seen:
         remove_front_of_list(seen, c)

      seen.append(c)
         
      if len(seen) == num:
         break;
   
   return count


def find_message_marker_in_buffer(buff):
   return find_string_of_different_chars_in_buffer(buff, 14)


def find_packet_marker_in_buffer(buff):
   return find_string_of_different_chars_in_buffer(buff, 4)


def remove_front_of_list(l1, item_to_remove_to):
   place = l1.index(item_to_remove_to)
   del l1[:place + 1]


def day_6_part_1(data):
   pos = find_packet_marker_in_buffer(data)

   print(f"Start-of-packet marker detected at position {pos}.")


def day_6_part_2(data):
   pos = find_message_marker_in_buffer(data)

   print(f"Start-of-message marker detected at position {pos}.")


def main():
   
   # open the data file
   with open('.\data\data.txt', 'r') as f:
      all_data = f.readline()

   day_6_part_1(all_data)
   day_6_part_2(all_data)


if __name__ == '__main__':
   main()
