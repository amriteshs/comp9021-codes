# Randomly fills a grid of size 7 x 7 with NE, SE, SW, NW,
# meant to represent North-East, South-East, North-West, South-West,
# respectively, and starting from the cell in the middle of the grid,
# determines, for each of the 4 corners of the grid, the preferred path amongst
# the shortest paths that reach that corner, if any. At a given cell, it is possible to move
# according to any of the 3 directions indicated by the value of the cell;
# e.g., from a cell storing NE, it is possible to move North-East, East, or North.
# At any given point, one prefers to move diagonally, then horizontally,
# and vertically as a last resort.
#
# Written by Amritesh Singh and Eric Martin for COMP9021


import sys
from random import seed, choice
from quiz09_queue_adt import *
from collections import defaultdict


def display_grid():
    for row in grid:
        print('    ', *row)


def preferred_paths_to_corners():
    found_paths = defaultdict(list)
    possible_paths = Queue()

    possible_paths.enqueue([(3, 3)])

    while not possible_paths.is_empty():
        x = possible_paths.dequeue()
        i = x[len(x) - 1][0]
        j = x[len(x) - 1][1]

        if grid[i][j] == 'NW':
            if i > 0 and j > 0 and (i - 1, j - 1) not in x:
                y = list(x)
                y.append((i - 1, j - 1))

                if (i - 1, j - 1) in corners:
                    if (i - 1, j - 1) not in found_paths:
                        found_paths[(i - 1, j - 1)] = y
                    elif len(y) < len(found_paths[(i - 1, j - 1)]):
                        found_paths[(i - 1, j - 1)] = y
                else:
                    possible_paths.enqueue(y)

            if j > 0 and (i, j - 1) not in x:
                y = list(x)
                y.append((i, j - 1))

                if (i, j - 1) in corners:
                    if (i, j - 1) not in found_paths:
                        found_paths[(i, j - 1)] = y
                    elif len(y) < len(found_paths[(i, j - 1)]):
                        found_paths[(i, j - 1)] = y
                else:
                    possible_paths.enqueue(y)

            if i > 0 and (i - 1, j) not in x:
                y = list(x)
                y.append((i - 1, j))

                if (i - 1, j) in corners:
                    if (i - 1, j) not in found_paths:
                        found_paths[(i - 1, j)] = y
                    elif len(y) < len(found_paths[(i - 1, j)]):
                        found_paths[(i - 1, j)] = y
                else:
                    possible_paths.enqueue(y)

        elif grid[i][j] == 'NE':
            if i > 0 and j < 6 and (i - 1, j + 1) not in x:
                y = list(x)
                y.append((i - 1, j + 1))

                if (i - 1, j + 1) in corners:
                    if (i - 1, j + 1) not in found_paths:
                        found_paths[(i - 1, j + 1)] = y
                    elif len(y) < len(found_paths[(i - 1, j + 1)]):
                        found_paths[(i - 1, j + 1)] = y
                else:
                    possible_paths.enqueue(y)

            if j < 6 and (i, j + 1) not in x:
                y = list(x)
                y.append((i, j + 1))

                if (i, j + 1) in corners:
                    if (i, j + 1) not in found_paths:
                        found_paths[(i, j + 1)] = y
                    elif len(y) < len(found_paths[(i, j + 1)]):
                        found_paths[(i, j + 1)] = y
                else:
                    possible_paths.enqueue(y)

            if i > 0 and (i - 1, j) not in x:
                y = list(x)
                y.append((i - 1, j))

                if (i - 1, j) in corners:
                    if (i - 1, j) not in found_paths:
                        found_paths[(i - 1, j)] = y
                    elif len(y) < len(found_paths[(i - 1, j)]):
                        found_paths[(i - 1, j)] = y
                else:
                    possible_paths.enqueue(y)

        elif grid[i][j] == 'SW':
            if i < 6 and j > 0 and (i + 1, j - 1) not in x:
                y = list(x)
                y.append((i + 1, j - 1))

                if (i + 1, j - 1) in corners:
                    if (i + 1, j - 1) not in found_paths:
                        found_paths[(i + 1, j - 1)] = y
                    elif len(y) < len(found_paths[(i + 1, j - 1)]):
                        found_paths[(i + 1, j - 1)] = y
                else:
                    possible_paths.enqueue(y)

            if j > 0 and (i, j - 1) not in x:
                y = list(x)
                y.append((i, j - 1))

                if (i, j - 1) in corners:
                    if (i, j - 1) not in found_paths:
                        found_paths[(i, j - 1)] = y
                    elif len(y) < len(found_paths[(i, j - 1)]):
                        found_paths[(i, j - 1)] = y
                else:
                    possible_paths.enqueue(y)

            if i < 6 and (i + 1, j) not in x:
                y = list(x)
                y.append((i + 1, j))

                if (i + 1, j) in corners:
                    if (i + 1, j) not in found_paths:
                        found_paths[(i + 1, j)] = y
                    elif len(y) < len(found_paths[(i + 1, j)]):
                        found_paths[(i + 1, j)] = y
                else:
                    possible_paths.enqueue(y)

        elif grid[i][j] == 'SE':
            if i < 6 and j < 6 and (i + 1, j + 1) not in x:
                y = list(x)
                y.append((i + 1, j + 1))

                if (i + 1, j + 1) in corners:
                    if (i + 1, j + 1) not in found_paths:
                        found_paths[(i + 1, j + 1)] = y
                    elif len(y) < len(found_paths[(i + 1, j + 1)]):
                        found_paths[(i + 1, j + 1)] = y
                else:
                    possible_paths.enqueue(y)

            if j < 6 and (i, j + 1) not in x:
                y = list(x)
                y.append((i, j + 1))

                if (i, j + 1) in corners:
                    if (i, j + 1) not in found_paths:
                        found_paths[(i, j + 1)] = y
                    elif len(y) < len(found_paths[(i, j + 1)]):
                        found_paths[(i, j + 1)] = y
                else:
                    possible_paths.enqueue(y)

            if i < 6 and (i + 1, j) not in x:
                y = list(x)
                y.append((i + 1, j))

                if (i + 1, j) in corners:
                    if (i + 1, j) not in found_paths:
                        found_paths[(i + 1, j)] = y
                    elif len(y) < len(found_paths[(i + 1, j)]):
                        found_paths[(i + 1, j)] = y
                else:
                    possible_paths.enqueue(y)

    # according to given coordinate system
    found_paths_new = defaultdict(list)

    if (0, 0) in found_paths:
        found_paths_new[(0, 0)] = found_paths[(0, 0)]

    if (6, 0) in found_paths:
        found_paths_new[(0, 6)] = found_paths[(6, 0)]

    if (6, 6) in found_paths:
        found_paths_new[(6, 6)] = found_paths[(6, 6)]

    if (0, 6) in found_paths:
        found_paths_new[(6, 0)] = found_paths[(0, 6)]

    for key, val in found_paths_new.items():
        new_v = []

        for v in val:
            new_v.append((v[1], v[0]))

        found_paths_new[key] = new_v

    return found_paths_new


try:
    seed_arg = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
size = 3
dim = 2 * size + 1
grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

grid = [[choice(directions) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
paths = preferred_paths_to_corners()
if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print(f'There is no path to {corner}')
    else:
        print(f'The preferred path to {corner} is:')
        print('  ', paths[corner])