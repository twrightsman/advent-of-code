import sys
import re

# Notes from Reddit Solution, courtesy of askalski
# First insight
# Only two (2) types of productions:
# 1.) e => XX and X => XX (X != Rn, Y, or Ar)
# 2.) X => X Rn X Ar | X Rn X Y X Ar | X Rn X Y X Y X Ar

# Second insight
# Rn Y Ar can be thought of as ( , )
# X => X (X) | X(X,X) | X(X,X,X)

# Third insight
# Repeated application of X => XX until single token takes 
#     count(token) - 1 steps
# X => X(X) similar to X => XX, except () is free, so takes
#     count(tokens) - count("(" or ")") - 1 steps
# X => X(X,X) each comma reduces length by two ",X", so takes
#     count(tokens) - count("(" or ")") - 2*count(",") - 1

# Final Solution
# Count tokens in input file
# Count Rn and Ar ("(" and ")")
# Count Y (",")
# Plug n' Chug

element_match_pattern = re.compile(r'([A-Z][a-z]?)')
final_molecule = str()

while True:
    line = sys.stdin.readline()
    if line == "\n":
        final_molecule = sys.stdin.readline().rstrip()
        break

results = re.findall(element_match_pattern, final_molecule)
tokens = len(results)
parenthesis = results.count('Rn') + results.count('Ar')
commas = results.count('Y')

minimum_steps = tokens - parenthesis - 2*commas - 1
print(minimum_steps)
