keypad = [["1", "2", "3"],
          ["4", "5", "6"],
          ["7", "8", "9"]]
coords = [1, 1]
password = ""

with open('day2_input.txt') as digit_instructions_file:
    for digit_instruction in digit_instructions_file:
        for direction in digit_instruction.rstrip():
            if direction == "U":
                if coords[0] > 0:
                    coords[0] -= 1
            if direction == "D":
                if coords[0] < 2:
                    coords[0] += 1
            if direction == "L":
                if coords[1] > 0:
                    coords[1] -= 1
            if direction == "R":
                if coords[1] < 2:
                    coords[1] += 1

        password += keypad[coords[0]][coords[1]]

print(password)
