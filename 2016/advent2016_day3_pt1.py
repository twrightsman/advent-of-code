with open('day3_input.txt') as triangles_file:
    possible_triangles = 0
    for triangle in triangles_file:
        # credit for learning that split() defaults to whitespace:
        # https://stackoverflow.com/questions/10974932/
        sides = [int(x.strip()) for x in triangle.split()] 
        hypotenuse = sides.pop(sides.index(max(sides)))
        
        if hypotenuse < sum(sides):
            possible_triangles += 1

print(possible_triangles)
