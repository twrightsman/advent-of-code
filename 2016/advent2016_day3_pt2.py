from itertools import islice

with open('day3_input.txt') as triangles_file:
    possible_triangles = 0
    # clever idiomatic use of zip from stackoverflow/python docs:
    # https://stackoverflow.com/questions/6890065/
    triangles_file_slices = list(zip(*[iter(triangles_file)]*3))
    for triangles_file_slice in triangles_file_slices:
        triangles = [[],[],[]]
        for triangle_triad in triangles_file_slice:
            sides = [int(x.strip()) for x in triangle_triad.split()]
            for i in range(0, 3):
                triangles[i].append(sides[i])
        
        for triangle in triangles:
            hypotenuse = triangle.pop(triangle.index(max(triangle)))
        
            if hypotenuse < sum(triangle):
                possible_triangles += 1

print(possible_triangles)
