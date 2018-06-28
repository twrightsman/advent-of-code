import sys
import ast

code_chars = 0
noncode_chars = 0

for line in sys.stdin:
    stripped_line = line.rstrip()
    code_chars += len(stripped_line)
    noncode_chars += len(ast.literal_eval(stripped_line))

print(code_chars - noncode_chars)