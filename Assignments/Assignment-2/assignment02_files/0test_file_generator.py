import os
from random import randint, choice

if __name__ == '__main__':
    x = randint(2, 42)
    y = randint(2, 32)
    grid = ''

    for i in range(x):
        for j in range(y):
            if i == x - 1 and j == y - 1:
                grid += '0'
            elif i == x - 1:
                grid += choice(['0', '1'])
            elif j == y - 1:
                grid += choice(['0', '2'])
            else:
                grid += choice(['0', '1', '2', '3'])

        grid += '\n'

    file_number = 1
    while True:
        if not os.path.isfile(f'maze_test{file_number}.txt'):
            with open(f'maze_test{file_number}.txt', 'w') as file:
                file.write(grid)

            break

        file_number += 1