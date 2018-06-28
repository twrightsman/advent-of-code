import sys

class LightGrid:
    def __init__(self, initial_state_grid):
        self.grid = {}
        self.height = len(initial_state_grid)
        self.width = len(initial_state_grid[0])
        for y, row in enumerate(initial_state_grid):
            for x, point in enumerate(row):
                if point == '#':
                    self.grid[(x, y)] = 1
                else:
                    self.grid[(x, y)] = 0

        #turn on corners
        self.grid[(0, 0)] = 1
        self.grid[(0, self.height - 1)] = 1
        self.grid[(self.width - 1, 0)] = 1
        self.grid[(self.width - 1, self.height - 1)] = 1

    def get_neighbors(self, x, y):
        neighbors = []
        for rel_x in range(-1, 2):
            for rel_y in range(-1, 2):
                if rel_x == 0 and rel_y == 0:
                    continue
                try:
                    neighbors.append(self.grid[(x + rel_x, y + rel_y)])
                except KeyError:
                    neighbors.append(0)

        return neighbors

    def update_point(self, x, y):
        corner = False
        #force corners on
        if x == 0:
            if y == 0:
                self.next_state[(x, y)] = 1
                corner = True
            if y == self.height - 1:
                self.next_state[(x, y)] = 1
                corner = True
        if x == self.width - 1:
            if y == 0:
                self.next_state[(x, y)] = 1
                corner = True
            if y == self.height - 1:
                self.next_state[(x, y)] = 1
                corner = True

        if not corner:
            neighbor_sum = sum(self.get_neighbors(x, y))
            if self.grid[(x, y)] == 1:
                if not (2 <= neighbor_sum <= 3):
                    self.next_state[(x, y)] = 0
                else:
                    self.next_state[(x, y)] = 1
            else:
                if neighbor_sum == 3:
                    self.next_state[(x, y)] = 1
                else:
                    self.next_state[(x, y)] = 0

    def step(self):
        self.next_state = {}
        for point in self.grid:
            self.update_point(*point)

        self.grid = self.next_state

    def output_grid(self):
        out = []
        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                row.append('#' if self.grid[(x, y)] == 1 else '.')
            out.append(''.join(row))
        return out

input_grid = sys.stdin.read().split('\n')
myLightGrid = LightGrid(input_grid)

for step in range(100):
    myLightGrid.step()

count = 0
for row in myLightGrid.output_grid():
    count += row.count('#')

print(count)