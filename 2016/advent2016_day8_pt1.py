from time import sleep

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.PIXEL_ON = '#'
        self.PIXEL_OFF = '.'
        self.PIXEL_ERROR = 'X'
        self.pixels = [[self.PIXEL_OFF for x in range(width)] for y in range(height)]

    def turn_on_pixel(self, x, y):
        self.pixels[y][x] = self.PIXEL_ON

    def turn_off_pixel(self, x, y):
        self.pixels[y][x] = self.PIXEL_OFF

    def count_pixels_on(self):
        count_on = 0
        for row in self.pixels:
            for pixel in row:
                if pixel == self.PIXEL_ON:
                    count_on += 1
        return count_on

    def parse_command(self, line):
        arguments = line.strip().split(' ')
        command = arguments.pop(0)
        getattr(self, 'command_' + command)(*arguments)

    def command_rect(self, dimensions):
        """turns on all of the pixels in a rectangle at the top-left of the
        screen which is A wide and B tall.
        """
        width, height = [int(ele) for ele in dimensions.split('x')]
        if (width <= self.width) and (height <= self.height):
            for y in range(0, height):
                for x in range(0, width):
                    self.turn_on_pixel(x, y)
        else:
            raise IndexError("Dimensions out of range for 'rect'")

    def command_rotate(self, obj, index_str, by_str, shift):
        axis, index = index_str.split('=')
        if (obj == 'row') and (axis == 'y'):
            self.rotate_row(int(index), int(shift))
        elif (obj == 'column') and (axis == 'x'):
            self.rotate_col(int(index), int(shift))
        else:
            raise ValueError("Invalid arguments for 'rotate'")

    def shift_list_right(self, l, shift):
        actual_shift = shift % len(l)
        out = [self.PIXEL_ERROR for i in range(len(l))]
        for i, e in enumerate(l):
            if i + actual_shift > (len(l) - 1):
                actual_shift = actual_shift - len(l)
            out[i + actual_shift] = e
        return out

    def rotate_row(self, index, shift):
        """shifts all of the pixels in row A (0 is the top row) right by B
        pixels. Pixels that would fall off the right end appear at the left
        end of the row.
        """
        self.pixels[index] = self.shift_list_right(self.pixels[index], shift)

    def rotate_col(self, index, shift):
        """shifts all of the pixels in column A (0 is the left column) down by
        B pixels. Pixels that would fall off the bottom appear at the top of
        the column.
        """
        column = [row[index] for row in self.pixels]
        new_column = self.shift_list_right(column, shift)
        for i in range(len(new_column)):
            self.pixels[i][index] = new_column[i]

    def __str__(self):
        out = ''
        for row in self.pixels:
            out += (''.join(row) + "\n")
        return out


little_screen = Screen(50, 6)
with open('day8_input.txt') as command_file:
    for command_line in command_file:
        little_screen.parse_command(command_line)

print(little_screen.count_pixels_on())
