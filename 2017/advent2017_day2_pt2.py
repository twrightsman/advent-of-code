from itertools import permutations

with open('advent2017_day2_input.txt') as day2_input:
  rows = []
  for row in day2_input:
    rows.append([int(ele) for ele in row.rstrip().split("\t")])

sum = 0
for row in rows:
  dividing_pairs = permutations(row, 2)
  for (numerator, denominator) in dividing_pairs:
    if numerator % denominator == 0:
      sum += numerator // denominator

print(sum)
