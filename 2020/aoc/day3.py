def day3_part1(submap: str) -> str:
    map_array = [line.rstrip() for line in submap.split("\n") if line.rstrip()]
    x, y = 0, 0

    trees_encountered = 0
    while y < len(map_array):
        trees_encountered += int(map_array[y][x] == '#')
        y += 1
        # wrap x around if too long
        x += 3
        if x >= len(map_array[0]):
            x -= len(map_array[0])

    return str(trees_encountered)

