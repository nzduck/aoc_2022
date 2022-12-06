
# open the data file
with open('.\data\data.txt', 'r') as f:
   all_data = f.readlines()

elf_num = 1
elf_total = 0
biggest_amount = 0
amount = 0

for l in all_data:
   stripped_line = l.strip()

   if len(stripped_line) != 0:         # we have found an amount being carried
      amount = int(stripped_line)      # amount being carried in this item
      elf_total += amount              # add to the total being carried by this elf
      print(f"Found amount {amount} for elf {elf_num} - total for elf is {elf_total}")
   else:                               # gap between elves
      if elf_total > biggest_amount:   # if the total for the previous elf is greater than the current total then
         biggest_amount = elf_total    # the current total becomes that amount being carried by the previous elf 
      
      elf_num += 1                     # inc the elf counter

      print(f"Moving on to elf {elf_num}.")
      amount = 0
      elf_total = 0

# post-process the final elf
if elf_total > biggest_amount:
   biggest_amount = elf_total

print(f"Largest single total being carried was {biggest_amount}.")

