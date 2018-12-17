import logging
import numpy as np
import re

fabric_size = (1001,1001)
claim_pattern = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

def solve_part1(input_file):
    fabric_matrix = np.zeros(fabric_size)
    for line in input_file:
        # parse the information
        # #(ID) @ (top_left_x),(top_left_y): (width)x(height)
        stripped_line = line.rstrip()
        match = claim_pattern.fullmatch(stripped_line)
        if match:
            claim_id = match.group(1)
            top_left_x = int(match.group(2))
            top_left_y = int(match.group(3))
            width = int(match.group(4))
            height = int(match.group(5))
            logging.debug("Parsed claim ID #{}, with top left coordinates ({},{}) and size {}x{} in".format(
                claim_id,
                top_left_x,
                top_left_y,
                width,
                height
            ))

            # mask the matrix with the rectangle (remember np matrix is row by column (y by x))
            # credit: https://stackoverflow.com/questions/30917753/subsetting-a-2d-numpy-array
            xv = np.linspace(top_left_x, top_left_x + width, width - 1, dtype = int)
            yv = np.linspace(top_left_y, top_left_y + height, height - 1, dtype = int)
            fabric_matrix[np.meshgrid(xv, yv, sparse = False, indexing = 'xy')] += 1
        else:
            logging.warning("Could not parse the claim: '{}'".format(stripped_line))
    return (fabric_matrix >= 2).sum()

def solve_part2(input_file):
    return None
