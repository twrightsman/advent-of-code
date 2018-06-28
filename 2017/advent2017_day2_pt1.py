with open('advent2017_day2_input.txt') as day2_input:
  rows = []
  for row in day2_input:
    rows.append([int(ele) for ele in row.rstrip().split("\t")])

sum = 0
for row in rows:
  sum += max(row) - min(row)

print(sum)
