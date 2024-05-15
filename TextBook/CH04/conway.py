import random, time, copy
WIDTH = 60
HEIGHT = 20

next_cells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')
        else:
            column.append(' ')
    next_cells.append(column)

while True:
    print('\n\n\n\n\n')
    current_cells = copy.deepcopy(next_cells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='')
        print()
    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left_coord = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            num_neighbors = 0
            if current_cells[left_coord][above_coord] == '#':
                num_neighbors += 1
            if current_cells[x][above_coord] == '#':
                num_neighbors += 1
            if current_cells[right_coord][above_coord] == '#':
                num_neighbors += 1
            if current_cells[left_coord][y] == '#':
                num_neighbors +=1
            if current_cells[right_coord][y] == '#':
                num_neighbors += 1
            if current_cells[left_coord][below_coord] == '#':
                num_neighbors += 1
            if current_cells[x][below_coord] == '#':
                num_neighbors += 1
            if current_cells[right_coord][below_coord] == '#':
                num_neighbors += 1

            if (current_cells[x][y] == '#' and(num_neighbors == 2 or num_neighbors == 3)):
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and num_neighbors == 3:
                next_cells[x][y] = '#'
            else:
                next_cells[x][y] = ' '
    time.sleep(1)