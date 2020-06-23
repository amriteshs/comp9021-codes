# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by Amritesh Singh and Eric Martin for COMP9021


from random import seed, randrange
import sys

dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end='')
        print(' '.join(grid[i][j] and '1' or '0' for j in range(dim)))
    print()


def possible_moves(x, y):
    possible_x = [x - 2, x - 1, x + 1, x + 2]
    possible_y = [y - 2, y - 1, y + 1, y + 2]

    possible_positions = [(i, j) for i in possible_x for j in possible_y if i in range(len(grid)) and \
                          j in range(len(grid)) and abs(i + j - x - y) % 2]

    return possible_positions


def possible_paths(x, y, p, v, k):
    moves_list = [(i, j) for i, j in possible_moves(x, y) if (i, j) in p and (i, j) not in v]

    if not moves_list:
        moves_list = [(i, j) for a, b in v for i, j in possible_moves(a, b) if (i, j) in p and (i, j) not in v]

    if len(v) is not len(p):
        if moves_list:
            v.append(moves_list[0])
            return possible_paths(moves_list[0][0], moves_list[0][1], p, v, k)

        k += 1
        new_position = [(i, j) for i, j in p if (i, j) not in v]
        v.append(new_position[0])
        return possible_paths(new_position[0][0], new_position[0][1], p, v, k)

    return k


def explore_board():
    position_of_ones = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j]]

    if position_of_ones:
        visited_cells = [position_of_ones[0]]
        return possible_paths(visited_cells[0][0], visited_cells[0][1], position_of_ones, visited_cells, 1)

    return 0


try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
nb_of_knights = explore_board()
if not nb_of_knights:
    print('No chess knight has explored this board.')
elif nb_of_knights == 1:
    print(f'At least 1 chess knight has explored this board.')
else:
    print(f'At least {nb_of_knights} chess knights have explored this board')
